import unittest
from textnode import TextNode, TextType
from spiltor import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_full_case(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_seperate_case(self):
        text = "This is an _italic_ word with **bold text** and [some link to boot.dev](https://boot.dev) also an image like ![genie image](https://i.imgur.com/fJRm4Vk.jpeg) with last word in `code section`"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word with ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("some link to boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" also an image like ", TextType.TEXT),
                TextNode("genie image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" with last word in ", TextType.TEXT),
                TextNode("code section", TextType.CODE),
            ],
            new_nodes,
        )

    def test_another_case(self):
        text = 'Block code "fences" Inline `code` with some [link text](http://dev.nodeca.com)'
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode('Block code "fences" Inline ', TextType.TEXT),
                TextNode('code', TextType.CODE),
                TextNode(' with some ', TextType.TEXT),
                TextNode('link text', TextType.LINK, "http://dev.nodeca.com"),
            ],
            new_nodes,
        )

    def test_text_with_no_markdown(self):
        text = "Syntax highlighting test-some-code"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode('Syntax highlighting test-some-code', TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
  unittest.main()