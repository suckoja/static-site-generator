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
