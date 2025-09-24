import unittest
from blocktype import BlockType
from spiltor import block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_normal_paragraph(self):
        block = "Just a normal text block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_h1_block(self):
        block = "# This is a h1 heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_h3_block(self):
        block = "### This is a h3 heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_h6_block(self):
        block = "###### This is a h6 heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_not_heading_block(self):
        block = "####### This is not a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_code_block_with_langauge(self):
        block = """```html
<dd>{{ $site->contact_infos }}</dd>
<dd>{!! $site->contact_infos !!}</dd>
<dt><strong>ข้อกำหนดการเข้าไซท์งาน</strong></dt>
<dd>{!! $site->access_rule !!}</dd>
<dt><strong>รายละเอียดไซท์งาน</strong></dt>
<dd>{{ $site->description }}</dd>
<dd>{!! $site->description !!}</dd>
```"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_code_block_without_language(self):
        block = "```\nno language here\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_multiple_code_blocks(self):
        block = "```py\nprint(1)\n```\n```bash\necho hi\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote_block(self):
        block = "> This is a quote."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_wrong_quote_block(self):
        block = ">This is not a quote."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_unordered_list_block(self):
        block = """\n- First item\n- Second item\n- Nested item"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_nested_list(self):
        block = """
* First item
* Second item
* Nested item
    - Inside item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_list_with_extra_spaces(self):
        block = "-   Trim me  "
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        block = """
1. Wash rice
2. Add water
3. Boil
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_nested_ordered_list_block(self):
        block = """
1. Wash rice
2. Add water
3. Boil
   1. Wait until done
   2. Let cool
4. Serve
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_with_trailing_space(self):
        md = "1.   Keep me neat   \n2.    Keep me tight     "
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

if __name__ == "__main__":
  unittest.main()