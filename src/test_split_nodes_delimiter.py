import unittest
from textnode import TextNode, TextType
from spilt_nodes_delimiter import split_nodes_delimiter

class TextSplitNodesDelimiter(unittest.TestCase):
  def test_code(self):
    node = TextNode(
      "This is text with a `code block` word", 
      TextType.TEXT
    )
    actual_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    expected_nodes = [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT),
    ]
    self.assertEqual(actual_nodes, expected_nodes)

  def test_bold(self):
    node = TextNode(
      "This is text with a **bolded phrase** in the middle",
      TextType.TEXT
    )
    actual_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    expected_nodes = [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("bolded phrase", TextType.BOLD),
      TextNode(" in the middle", TextType.TEXT),
    ]
    self.assertEqual(actual_nodes, expected_nodes)

  def test_italic(self):
    node = TextNode(
      "This is an _italic and **bold** word_.",
      TextType.TEXT
    )
    actual_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    expected_nodes = [
      TextNode("This is an ", TextType.TEXT),
      TextNode("italic and **bold** word", TextType.ITALIC),
      TextNode(".", TextType.TEXT),
    ]
    self.assertEqual(actual_nodes, expected_nodes)

  def test_non_split(self):
    node = TextNode("**This is a bold text**", TextType.TEXT)
    actual_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    expected_nodes = [
      TextNode("This is a bold text", TextType.BOLD),
    ]
    self.assertEqual(actual_nodes, expected_nodes)

  def test_multiple_occurances_in_one_old_node(self):
    node = TextNode("This is **many** more **times with **a **bold** text.", TextType.TEXT)
    actual_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    expected_nodes = [
      TextNode("This is ", TextType.TEXT),
      TextNode("many", TextType.BOLD),
      TextNode(" more ", TextType.TEXT),
      TextNode("times with ", TextType.BOLD),
      TextNode("a ", TextType.TEXT),
      TextNode("bold", TextType.BOLD),
      TextNode(" text.", TextType.TEXT),
    ]
    self.assertEqual(actual_nodes, expected_nodes)

  def test_multiple_old_nodes(self):
    node1 = TextNode("**First sentences**", TextType.TEXT)
    node2 = TextNode("I don't wanna **miss** a thing", TextType.TEXT)
    node3 = TextNode("Liverpool **3 - 2** Athetico Madrid", TextType.TEXT)
    actual_nodes = split_nodes_delimiter([
      node1, node2, node3
    ], "**", TextType.BOLD)
    expected_nodes = [
      TextNode("First sentences", TextType.BOLD),
      TextNode("I don't wanna ", TextType.TEXT),
      TextNode("miss", TextType.BOLD),
      TextNode(" a thing", TextType.TEXT),
      TextNode("Liverpool ", TextType.TEXT),
      TextNode("3 - 2", TextType.BOLD),
      TextNode(" Athetico Madrid", TextType.TEXT),
    ]
    self.assertEqual(actual_nodes, expected_nodes)

  def test_not_text_type(self):
    node1 = TextNode("I don't _wanna miss_ a thing", TextType.ITALIC)
    node2 = TextNode(
      "This is an _italic word_.",
      TextType.TEXT
    )
    actual_nodes = split_nodes_delimiter([node1, node2], "_", TextType.ITALIC)
    expected_nodes = [
      TextNode("I don't _wanna miss_ a thing", TextType.ITALIC),
      TextNode("This is an ", TextType.TEXT),
      TextNode("italic word", TextType.ITALIC),
      TextNode(".", TextType.TEXT),
    ]
    self.assertEqual(actual_nodes, expected_nodes)

  def test_matching_closing_delimiter_is_not_found(self):
    node = TextNode("I don't _close** my eye", TextType.TEXT)
    with self.assertRaisesRegex(Exception, "Invalid Markdown syntax"):
      actual_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

  def test_no_matching_delimiter_in_text(self):
    node = TextNode("Baby Baby _Baby_ Ohh!!", TextType.TEXT)
    actual_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    expected_nodes = [
      TextNode("Baby Baby _Baby_ Ohh!!", TextType.TEXT),
    ]
    self.assertEqual(actual_nodes, expected_nodes)

if __name__ == "__main__":
  unittest.main()