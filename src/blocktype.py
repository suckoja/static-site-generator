from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "p",
    HEADING = "h1",
    CODE = "code",
    QUOTE = "blockquote",
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"