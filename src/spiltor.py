import re
from textnode import TextNode, TextType
from extractor import extract_markdown_between,  extract_markdown_links, extract_markdown_images, extract_markdown_ordered_lists
from blocktype import BlockType

def get_target_texts(old_text, delimiter):
  targets = []
  target_text = ''
  while target_text != None:
    target_text = extract_markdown_between(old_text, delimiter, delimiter)
    targets.append(target_text)
    old_text = old_text.replace(f"{delimiter}{target_text}{delimiter}", "", 1)
  return targets

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    target_texts = get_target_texts(old_node.text, delimiter)

    texts = old_node.text.split(delimiter)
    for text in texts:
      if not text:
         continue
      elif text in target_texts:
        new_node = TextNode(text, text_type)
      else:
        new_node = TextNode(text, TextType.TEXT)
      new_nodes.append(new_node)
  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []
  for old_node in old_nodes:

    # link extractor
    link_extractors = extract_markdown_links(old_node.text)

    # now, we need to split texts
    old_text = old_node.text
    for extract in link_extractors:
      target = f"[{extract['text']}]({extract['href']})"

      # check to see do we have TextType.TEXT before
      sections = old_text.split(target, 1)
      if len(sections) > 0 and sections[0] != "":
        if not extract_markdown_links(sections[0]):
          new_nodes.append(
            TextNode(sections[0], TextType.TEXT)
          )
          old_text = old_text.replace(sections[0], "", 1)

      # append LINK while remove extract text from old_text
      new_nodes.append(
        TextNode(extract['text'], TextType.LINK, extract['href'])
      )
      old_text = old_text.replace(target, "", 1)

  return new_nodes

def split_nodes_image(old_nodes):
  new_nodes = []
  for old_node in old_nodes:

    # link extractor
    link_extractors = extract_markdown_images(old_node.text)

    # now, we need to split texts
    old_text = old_node.text
    for extract in link_extractors:
      target = f"![{extract['alt']}]({extract['src']})"

      # check to see do we have TextType.TEXT before
      sections = old_text.split(target, 1)
      if len(sections) > 0 and sections[0] != "":
        if not extract_markdown_images(sections[0]):
          new_nodes.append(
            TextNode(sections[0], TextType.TEXT)
          )
          old_text = old_text.replace(sections[0], "", 1)

      # append IMAGE while remove extract text from old_text
      new_nodes.append(
        TextNode(extract['alt'], TextType.IMAGE, extract['src'])
      )
      old_text = old_text.replace(target, "", 1)

  return new_nodes

def combine_text_node_to_string(nodes):
  result = ""
  for node in nodes:
    if node.text_type == TextType.TEXT:
      result += node.text
    elif node.text_type == TextType.BOLD:
      result += f"**{node.text}**"
    elif node.text_type == TextType.ITALIC:
      result += f"_{node.text}_"
    elif node.text_type == TextType.CODE:
      result += f"`{node.text}`"
    elif node.text_type == TextType.LINK:
      result += f"[{node.text}]({node.url})"
    elif node.text_type == TextType.IMAGE:
      result += f"![{node.text}]({node.url})"
  return result

def find_first_occurring_substring(main_string, target_substrings):
    min_index = float('inf')
    first_found_substring = None

    for target in target_substrings:
        index = main_string.find(target)
        if index != -1 and index < min_index:
            min_index = index
            first_found_substring = target
    
    return first_found_substring

def text_to_textnodes(text):
  targets = ["**", "![", "_", "`", "["]
  new_nodes = []
  old_text = text

  while old_text:
    # find first match 
    first_match = find_first_occurring_substring(old_text, targets)
    node = TextNode(old_text, TextType.TEXT)
    match first_match:
      case "**":
        nodes = split_nodes_delimiter([node], first_match, TextType.BOLD)
        if len(nodes) > 2:
          new_nodes.extend(nodes[:-1])
          to_remove = combine_text_node_to_string(nodes[:-1])
        else:
          new_nodes.extend(nodes)
          to_remove = combine_text_node_to_string(nodes)
        old_text = old_text.replace(to_remove, "", 1)
      case "_":
        nodes = split_nodes_delimiter([node], first_match, TextType.ITALIC)
        if len(nodes) > 2:
          new_nodes.extend(nodes[:-1])
          to_remove = combine_text_node_to_string(nodes[:-1])
        else:
          new_nodes.extend(nodes)
          to_remove = combine_text_node_to_string(nodes)
        old_text = old_text.replace(to_remove, "", 1)
      case "`":
        nodes = split_nodes_delimiter([node], first_match, TextType.CODE)
        if len(nodes) > 2:
          new_nodes.extend(nodes[:-1])
          to_remove = combine_text_node_to_string(nodes[:-1])
        else:
          new_nodes.extend(nodes)
          to_remove = combine_text_node_to_string(nodes)
        old_text = old_text.replace(to_remove, "", 1)
      case "![":
        nodes = split_nodes_image([node])
        if len(nodes) > 2:
          new_nodes.extend(nodes[:-1])
          to_remove = combine_text_node_to_string(nodes[:-1])
        else:
          new_nodes.extend(nodes)
          to_remove = combine_text_node_to_string(nodes)
        old_text = old_text.replace(to_remove, "", 1)
      case "[":
        nodes = split_nodes_link([node])
        if len(nodes) > 2:
          new_nodes.extend(nodes[:-1])
          to_remove = combine_text_node_to_string(nodes[:-1])
        else:
          new_nodes.extend(nodes)
          to_remove = combine_text_node_to_string(nodes)
        old_text = old_text.replace(to_remove, "", 1)
      case _:
        new_nodes.append(TextNode(old_text, TextType.TEXT))
        old_text = old_text.replace(old_text, "", 1)
  
  return new_nodes

def markdown_to_blocks(markdown):
  blocks = []
  splits = markdown.split('\n\n')
  for item in splits:
    if item != "":
      blocks.append(item.strip())
  return blocks

def block_to_block_type(block):
  block = block.strip()
  if re.findall(r'^#{1,6}\s(.+)', block):
    return BlockType.HEADING
  elif re.findall(r"```(?:([a-zA-Z0-9]+)\n)?([\s\S]*?)```", block):
    return BlockType.CODE
  elif re.findall(r"\>\s(.+)", block):
    return BlockType.QUOTE
  elif re.findall(r"^[ \t]*[-*+][ \t]+(.*)", block):
    return BlockType.UNORDERED_LIST
  elif re.findall(r"^[ \t]*\d+\.[ \t]+(.*)", block):
    return BlockType.ORDERED_LIST
  else:
    return BlockType.PARAGRAPH
  
def split_markdown_unordered_list(markdown_text):
    """
    Splits a Markdown unordered list into a list of individual list items.
    Handles nested lists by preserving their indentation.
    """
    lines = markdown_text.strip().split('\n')
    list_items = []
    current_item = []

    for line in lines:
        # Check if the line starts a new top-level list item
        # or if it's a continuation of a previous item (e.g., a paragraph within an item)
        # or a nested item.
        if line.lstrip().startswith(('* ', '- ', '+ ')) and not current_item:
            # Start a new item
            current_item.append(line)
        elif line.lstrip().startswith(('* ', '- ', '+ ')) and current_item:
            # New list item, so append the previous one and start a new one
            list_items.append('\n'.join(current_item))
            current_item = [line]
        elif current_item:
            # Continuation of the current item (e.g., a multi-line paragraph or nested content)
            current_item.append(line)
        else:
            # If it's not a list item and no item is being built, ignore or handle as non-list content
            pass

    # Append the last item if it exists
    if current_item:
        list_items.append('\n'.join(current_item))

    return list_items

def split_markdown_ordered_list(markdown_text):
  return extract_markdown_ordered_lists(markdown_text)