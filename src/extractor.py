import re

def extract_markdown_between(text, substring1, substring2):
    """
    Extracts the substring between two specified characters in a given string.

    Args:
        text (str): The input string.
        substring (str): The substring to check.

    Returns:
        str: The substring between char1 and char2, or an empty string if
             either character is not found or if char2 appears before char1.
    """
    start_index = text.find(substring1)
    if start_index == -1:
        return None  # first substring not found
    
    content_start_index = start_index + len(substring1)

    end_index = text.find(substring2, content_start_index)
    if end_index == -1:
        raise Exception("Invalid Markdown syntax")

    return text[content_start_index:end_index]

def extract_markdown_links(text):
    """
    Extract normal markdown links: [text](url)
    """
    matches = re.findall(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)', text)
    return [
        {"type": "link", "text": text, "href": href}
        for text, href in matches
    ]


def extract_markdown_images(text):
    """
    Extract markdown images: ![alt](src "optional title")
    """
    matches = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)
    return [
        {"type": "image", "alt": alt, "src": src}
        for alt, src in matches
    ]


def extract_markdown_linked_images(text):
    """
    Extract linked images: [![alt](src)](href)
    """
    matches = re.findall(r'\[(!\[.*?\]\(.*?\))\]\(([^)]+)\)', text)
    return [
        {
            "type": "linked_image",
            "image_markdown": image_md,
            "href": href,
        }
        for image_md, href in matches
    ]

def extract_markdown_ordered_lists(text):
    list_item_pattern = re.compile(r'^\s*(\d+\.|[a-zA-Z]+\.)\s+(.*)', re.MULTILINE)
    matches = list_item_pattern.findall(text)
    return [
        {
            "type": "ordered_list",
            "text": content
        }
        for prefix, content in matches
    ]

def extract_markdown_blockquote(text):
    pattern = re.compile(r'^[ ]?>[ ]?(.*)', re.MULTILINE)

    # Find all matches and join consecutive lines that belong to the same blockquote.
    all_lines = pattern.findall(text)
    blockquotes = []
    current_quote = []

    for line in all_lines:
        if line.strip() == '':
            # A blank line can indicate the end of a blockquote.
            if current_quote:
                blockquotes.append('\n'.join(current_quote))
                current_quote = []
        else:
            current_quote.append(line)

    # Append the last blockquote if it exists
    if current_quote:
        blockquotes.append('\n'.join(current_quote))

    return blockquotes

def extract_markdown_heading(text):
    pattern = re.compile(r'^(#{1,6})\s(.*)', re.MULTILINE)
    matches = pattern.findall(text)
    return [
        {
            "type": "heading",
            "level": len(marker),
            "text": text,
        }
        for marker, text in matches
    ]
