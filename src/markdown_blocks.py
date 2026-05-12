from enum import Enum
from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import *

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    U_LIST = 'unordered_list'
    O_LIST = 'ordered_list'

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
            return BlockType.HEADING
    #multiline code
    multi_line = block.split("\n")
    if (len(multi_line) > 1 and
        multi_line[0] == "```" and 
        multi_line[-1] == "```"):
        return BlockType.CODE
    #quote block/paragraph
    if block.startswith(">"):
        for line in multi_line:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    #unordered
    if block.startswith("- "):
        for line in multi_line:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.U_LIST
    #ordered
    if block.startswith("1. "):
        for i in range(len(multi_line)):
            if not multi_line[i].startswith(f"{i + 1}. "):
                return BlockType.PARAGRAPH
        return BlockType.O_LIST
    #paragraph
    return BlockType.PARAGRAPH

def text_to_children(text):
    t_types = text_to_textnodes(text)
    children = []
    
    for t in t_types:
        children.append(text_node_to_html_node(t))
    return children
   

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html = []

    for b in blocks:
        b_type = block_to_block_type(b)
        if b_type == BlockType.PARAGRAPH:
            text = b.replace("\n", " ")
            html.append(ParentNode("p", text_to_children(text)))

        elif b_type == BlockType.HEADING:
            h_count = 0
            while b[h_count] == '#':
                h_count += 1
            normalized_b = b[h_count + 1:]
            html.append(ParentNode(f"h{h_count}", text_to_children(normalized_b)))

        elif b_type == BlockType.QUOTE:
            lines = b.split("\n")
            cleaned = []
            for line in lines:
                normalized_line = line.lstrip(">").strip()
                cleaned.append(normalized_line)
            text = " ".join(cleaned)
            html.append(ParentNode("blockquote", text_to_children(text)))

        elif b_type == BlockType.U_LIST:
            lines = b.split("\n")
            cleaned = []
            
            for line in lines:
                normalized_line = line.lstrip("-").strip()
                node = ParentNode("li", text_to_children(normalized_line))
                cleaned.append(node)
            html.append(ParentNode("ul", cleaned))

        elif b_type == BlockType.O_LIST:
            lines = b.split("\n")
            cleaned = []
            
            for line in lines:
                parts = line.split(". ", 1)
                normalized_line = parts[1]
                node = ParentNode("li", text_to_children(normalized_line))
                cleaned.append(node)
            html.append(ParentNode("ol", cleaned))

        elif b_type == BlockType.CODE:
            code_text = b[4:-3]
            text_node = TextNode(code_text, TextType.TEXT)
            html_node = text_node_to_html_node(text_node)
            code_html = ParentNode("code", [html_node])
            pre_wrap = ParentNode("pre", [code_html])
            html.append(pre_wrap)
    return ParentNode("div", html)
