import unittest
from htmlnode import HTMLNode

class TextTextNode(unittest.TestCase):
  def test_to_html_failed(self):
    node = HTMLNode()
    self.assertRaises(NotImplementedError, node.to_html)

  def test_link_props_to_html(self):
    props = {
      "href": "https://erp.sitem.co.th", 
      "target": "_blank", 
      "rel": "alternate", 
      "referrerpolicy": "origin"
    }
    node = HTMLNode('a', 'anchor test text', None, props)

    test_text = f"href=\"{props["href"]}\" target=\"{props["target"]}\" rel=\"{props["rel"]}\" referrerpolicy=\"{props["referrerpolicy"]}\""
    self.assertEqual(node.props_to_html(), test_text)

  def test_props_to_html_no_space_behind(self):
    props = {
      "src": "https://dummyimage.com/600x400/000/fff.png",
      "alt": "test dummy image",
      "width": "500",
      "height": "600"
    }
    node = HTMLNode('img', None, None, props)

    test_text = f"src=\"{props["src"]}\" alt=\"{props["alt"]}\" width=\"{props["width"]}\" height=\"{props["height"]}\" "
    self.assertNotEqual(node.props_to_html(), test_text)

if __name__ == "__main__":
  unittest.main()