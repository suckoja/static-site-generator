import unittest
from textnode import TextNode, TextType
from convert import text_node_to_html_node

class TextConvert(unittest.TestCase):
  def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")
    self.assertEqual(html_node.to_html(), "This is a text node")

  def test_bold(self):
    node = TextNode("This is a bold text", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is a bold text")
    self.assertEqual(html_node.to_html(), "<b>This is a bold text</b>")

  def test_italic(self):
    node = TextNode("This is a italic text", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "This is a italic text")
    self.assertEqual(html_node.to_html(), "<i>This is a italic text</i>")

  def test_code(self):
    node = TextNode("This is a code text", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "This is a code text")
    self.assertEqual(html_node.to_html(), "<code>This is a code text</code>")

  def test_link(self):
    node = TextNode("Please click us", TextType.LINK, "https://www.google.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "Please click us")
    self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">Please click us</a>')

  def test_image(self):
    node = TextNode("Dummy Image", TextType.IMAGE, "https://dummyimage.com/600x400/000/fff.png")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.to_html(), '<img src="https://dummyimage.com/600x400/000/fff.png" alt="Dummy Image">')

  def test_type_attribute_error(self):
    with self.assertRaises(AttributeError):
      node = TextNode("This is some text node", TextType.ETC)
      html_node = text_node_to_html_node(node)

  def test_none_type_error(self):
    with self.assertRaises(TypeError):
      node = TextNode("This is some text node")
      html_node = text_node_to_html_node(node)

if __name__ == "__main__":
  unittest.main()