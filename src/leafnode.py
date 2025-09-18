from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if not self.value:
      raise ValueError("Leaf nodes must have a value.")
    elif self.tag is None:
      return self.value
    else:
      return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
  def props_to_html(self):
    return super().props_to_html()