import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_paragraph(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_leaf_to_html_bold(self):
    node = LeafNode("b", "This is a bold text")
    self.assertEqual(node.to_html(), "<b>This is a bold text</b>")

  def test_leaf_to_html_italic(self):
    node = LeafNode("i", "This is an italic text")
    self.assertEqual(node.to_html(), "<i>This is an italic text</i>")

  def test_leaf_to_html_anchor(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

  def test_leaf_to_html_no_value(self):
    node = LeafNode("p", None)
    self.assertRaises(ValueError, node.to_html)

  def test_leaf_to_html_empty_value(self):
    node = LeafNode("p", "")
    self.assertRaises(ValueError, node.to_html)

  def test_leaf_to_html_tag_is_none(self):
    node = LeafNode(None, "This is a test")
    self.assertEqual(node.to_html(), "This is a test")

if __name__ == "__main__":
  unittest.main()