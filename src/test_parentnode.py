import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_great_grandchild(self):
    great_grandchild_node = LeafNode("b", "great grandchild")
    grandchild_node = ParentNode("span", [great_grandchild_node])
    child_node = ParentNode("p", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><p><span><b>great grandchild</b></span></p></div>",
    )

  def test_to_html_with_mixed_children(self):
    node = ParentNode("p", [
      LeafNode("b", "Bold text"),
      LeafNode(None, "Normal text"),
      LeafNode("i", "italic text"),
      LeafNode(None, "Normal text"),
      ParentNode("div", [
        LeafNode("i", "Another italic text"),
        LeafNode(None, "text inside parent node"),
        LeafNode("b", "Another bold text"),
      ]),
    ])
    self.assertEqual(
        node.to_html(),
        "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<div><i>Another italic text</i>text inside parent node<b>Another bold text</b></div></p>"
    )

  def test_to_html_no_tag(self):
    node = ParentNode("", "some value")
    with self.assertRaisesRegex(ValueError, "Parent nodes must have a tag."): 
      node.to_html()

  def test_to_html_children_missing_value(self):
    node = ParentNode("div", [])
    with self.assertRaisesRegex(ValueError, "Children is missing a value."):
      node.to_html()

if __name__ == "__main__":
  unittest.main()