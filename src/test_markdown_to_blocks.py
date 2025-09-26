import unittest
from spiltor import markdown_to_blocks

class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """# This is a heading

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is the first list item in a list block
- This is a list item
- This is another list item
"""  
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ],
        )

    def test_another_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_yet_another_markdown_to_blocks(self):
        md = markdown_text = """
# My Title

This is a paragraph with **bold text** and *italic text*.

- Item 1
- Item 2

Here's some `inline code`.

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# My Title",
                "This is a paragraph with **bold text** and *italic text*.",
                "- Item 1\n- Item 2",
                "Here's some `inline code`.",
            ]
        )

if __name__ == "__main__":
  unittest.main()