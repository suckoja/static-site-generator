import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkDownToBlocks(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_paragraph_with_image_and_link(self):
        md = """
This is another paragraph with _italic_ text and `code` here

[OpenAI](https://openai.com)

![Alt text](https://via.placeholder.com/100)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><p><a href="https://openai.com">OpenAI</a></p><p><img src="https://via.placeholder.com/100" alt="Alt text"></p></div>',
        )

    def test_mixed_paragraph_with_code(self):
        md = """
This is `a test` _italic text_ with **bold text**

```
This is going _to_ get **tricky**
Like for real!
```

Please come visit us at [OpenAI](https://openai.com). Please enjoy this image first ![Alt text](https://via.placeholder.com/100) here.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is <code>a test</code> <i>italic text</i> with <b>bold text</b></p><pre><code>This is going _to_ get **tricky**\nLike for real!\n</code></pre><p>Please come visit us at <a href="https://openai.com">OpenAI</a>. Please enjoy this image first <img src="https://via.placeholder.com/100" alt="Alt text"> here.</p></div>',
        )

    def test_ordered_and_unordred_list(self):
        md = """
- Item 1
- Item 2
- Item 3

1. First
2. Second
3. Third
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><ol><li>First</li><li>Second</li><li>Third</li></ol></div>'
        )

    def test_blockquote(self):
        md = """
This is some regular text.

> This is a blockquote.
> It can span multiple lines.

Some text **in between**

> This is another,
> separate blockquote,
> but not a Haiku.

Regular text continues here.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is some regular text.</p><blockquote>This is a blockquote.\nIt can span multiple lines.</blockquote><p>Some text <b>in between</b></p><blockquote>This is another,\nseparate blockquote,\nbut not a Haiku.</blockquote><p>Regular text continues here.</p></div>'
        )

    def test_headings(self):
        md = """
# This is a Top-Level Heading

Here is some text under the first heading. It can span multiple lines.

## This is a Subheading

Content for the subheading goes here. It might have `inline code` or **bold** text.

### Nested Heading

This is content under a nested heading.

# Another Top-Level Heading

More content here, for a new top-level section.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>This is a Top-Level Heading</h1><p>Here is some text under the first heading. It can span multiple lines.</p><h2>This is a Subheading</h2><p>Content for the subheading goes here. It might have <code>inline code</code> or <b>bold</b> text.</p><h3>Nested Heading</h3><p>This is content under a nested heading.</p><h1>Another Top-Level Heading</h1><p>More content here, for a new top-level section.</p></div>'
        )

if __name__ == "__main__":
  unittest.main()