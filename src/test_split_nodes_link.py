import unittest
from textnode import TextNode, TextType
from spiltor import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_spilt_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ], new_nodes)

    def test_spilt_pure_links_with_no_text_between(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ], new_nodes)

    def test_spilt_links_with_only_text_between(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) I want it that way [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" I want it that way ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ], new_nodes)

    def test_spilt_links_with_only_text_between(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) I want it that way [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" I want it that way ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ], new_nodes)

if __name__ == "__main__":
  unittest.main()