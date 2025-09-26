from htmlnode import HTMLNode
from blocktype import BlockType
from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode
from extractor import extract_markdown_between, extract_markdown_blockquote, extract_markdown_heading
from spiltor import markdown_to_blocks, block_to_block_type, text_to_textnodes, split_markdown_unordered_list, split_markdown_ordered_list

def text_node_to_leaf_node(node):
    clean_text = node.text.replace('\n', ' ')
    if node.text_type == TextType.BOLD:
        return LeafNode("b", clean_text)
    elif node.text_type == TextType.ITALIC:
        return LeafNode("i", clean_text)
    elif node.text_type == TextType.CODE:
        return LeafNode("code", clean_text)
    elif node.text_type == TextType.LINK:
        return LeafNode("a", clean_text, {"href": node.url})
    elif node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": node.url, "alt": clean_text})
    else:
        return LeafNode(None, clean_text)

def text_nodes_to_children(text_nodes):
    children = []
    for text_node in text_nodes:
        leaf_node = text_node_to_leaf_node(text_node)
        children.append(leaf_node)
    return children


def unordered_list_to_children(block):
    children = []
    split_list = split_markdown_unordered_list(block)
    for item in split_list:
        leaf_node = LeafNode("li", item.replace("- ", ""))
        children.append(leaf_node)
    return children

def ordered_list_to_children(block):
    children = []
    split_list = split_markdown_ordered_list(block)
    for item in split_list:
        leaf_node = LeafNode("li", item['text'])
        children.append(leaf_node)
    return children

def parent_node_from_block(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.CODE:
        code_text = extract_markdown_between(block, '```', '```')
        clean_text = code_text.lstrip().replace('\r\n', 'n')
        return ParentNode('pre', [LeafNode("code", clean_text)])
    elif block_type == BlockType.UNORDERED_LIST:
        children = unordered_list_to_children(block)
        return ParentNode('ul', children)
    elif block_type == BlockType.ORDERED_LIST:
        children = ordered_list_to_children(block)
        return ParentNode('ol', children)
    elif block_type == BlockType.QUOTE:
        results = extract_markdown_blockquote(block)
        children = [LeafNode(None, results[0])]
        return ParentNode('blockquote', children)
    elif block_type == BlockType.HEADING:
        results = extract_markdown_heading(block)
        return LeafNode(f'h{results[0]['level']}', results[0]['text'])
    else:
        text_nodes = text_to_textnodes(block)
        children = text_nodes_to_children(text_nodes)
        return ParentNode('p', children)
    

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(parent_node_from_block(block))
    result = ParentNode("div", children)
    return result