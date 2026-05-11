from enum import Enum

class BlockType(Enum):
    paragraph = 'paragraph'
    heading = 'heading'
    code = 'code'
    quote = 'quote'
    unordered_list = 'unordered_list'
    ordered_list = 'ordered_list'

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    res = []

    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            new_lines.append(line.strip())
        res.append("\n".join(new_lines))
    return res

def block_to_block_type(block):
    #heading
    for i in range(1, 7):
        if block.startswith("#" * i + " "):
            return BlockType.heading
    #multiline code
    multi_line = block.split("\n")
    if (len(multi_line) > 1 and
        multi_line[0] == "```" and 
        multi_line[-1] == "```"):
        return BlockType.code
    #quote block/paragraph
    if block.startswith(">"):
        for line in multi_line:
            if not line.startswith(">"):
                return BlockType.paragraph
        return BlockType.quote
    #unordered
    if block.startswith("- "):
        for line in multi_line:
            if not line.startswith("- "):
                return BlockType.paragraph
        return BlockType.unordered_list
    #ordered
    if block.startswith("1. "):
        for i in range(len(multi_line)):
            if not multi_line[i].startswith(f"{i + 1}. "):
                return BlockType.paragraph
        return BlockType.ordered_list
    #paragraph
    return BlockType.paragraph