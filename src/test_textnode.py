import unittest
from textnode import TextNode, TextType

class TextTextNode(unittest.TestCase):
  def test_eq(self):
    n1 = TextNode('Test bold text', TextType.BOLD)
    n2 = TextNode('Test bold text', TextType.BOLD)
    self.assertEqual(n1, n2)

  def test_link_eq(self):
    n1 = TextNode('Anchor text', TextType.LINK, 'https://erp.sitem.co.th')
    n2 = TextNode('Anchor text', TextType.LINK, 'https://erp.sitem.co.th')
    self.assertEqual(n1, n2)

  def test_not_eq(self):
    n1 = TextNode('Test italic text', TextType.ITALIC)
    n2 = TextNode('Anchor text', TextType.LINK, 'https://erp.sitem.co.th')
    self.assertNotEqual(n1, n2)

  def test_type_property_not_eq(self):
    n1 = TextNode('Test italic text', TextType.IMAGE, 'https://erp.sitem.co.th')
    n2 = TextNode('Test italic text', TextType.LINK, 'https://erp.sitem.co.th')
    self.assertNotEqual(n1, n2)

  def test_link_not_eq(self):
    n1 = TextNode('Anchor text', TextType.LINK, 'https://erp.sitem.co.th')
    n2 = TextNode('Anchor text', TextType.LINK, 'https://erp.sitem.co.th/')
    self.assertNotEqual(n1, n2)

if __name__ == "__main__":
  unittest.main()