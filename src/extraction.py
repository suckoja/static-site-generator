import re

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
