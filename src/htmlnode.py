class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError('Not implement yet!')

  def props_to_html(self):
    html = ''
    if self.props is None:
      return html
    for prop in self.props:
      html += f' {prop}="{self.props[prop]}"'
    return html

  def __repr__(self):
    return (f"HTMLNode(\n"
            f"  tag={self.tag},\n"
            f"  value={self.value},\n"
            f"  children={self.children},\n"
            f"  props={self.props},\n"
            f")")