from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if not self.tag:
      raise ValueError("Parent nodes must have a tag.")
    elif not self.children:
      raise ValueError("Children is missing a value.")
    else:
      children_result = ''
      for child in self.children:
        children_result += child.to_html()
      return f"<{self.tag}{self.props_to_html()}>{children_result}</{self.tag}>"
  
  def props_to_html(self):
    return super().props_to_html()