from textnode import TextNode, TextType

def get_string_between(text, substring):
    """
    Extracts the substring between two specified characters in a given string.

    Args:
        text (str): The input string.
        substring (str): The substring to check.

    Returns:
        str: The substring between char1 and char2, or an empty string if
             either character is not found or if char2 appears before char1.
    """
    start_index = text.find(substring)
    if start_index == -1:
        return None  # first substring not found
    
    content_start_index = start_index + len(substring)

    end_index = text.find(substring, content_start_index)
    if end_index == -1:
        raise Exception("Invalid Markdown syntax")

    return text[content_start_index:end_index]

def get_target_texts(old_text, delimiter):
  targets = []
  target_text = ''
  while target_text != None:
    target_text = get_string_between(old_text, delimiter)
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