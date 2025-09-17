from textnode import TextNode
from textnode import TextType

def main():
  b = TextNode('Test bold text', TextType.BOLD)
  l = TextNode('Test Anchor Text', TextType.LINK, 'https://www.boot.dev')

  print(b)
  print(l)


if __name__ == "__main__":
  main()