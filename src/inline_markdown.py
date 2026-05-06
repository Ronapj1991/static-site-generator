import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        pieces = node.text.split(delimiter)

        if len(pieces) % 2 == 0:
            raise Exception("invalid markdown: unbalanced")

        for i in range(len(pieces)):
            if pieces[i] == "":
                continue
            if i % 2 == 0:
                new_list.append(TextNode(pieces[i], TextType.TEXT))
            else:
                new_list.append(TextNode(pieces[i], text_type))
    return new_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        remaining = node.text
        if len(images) == 0:
            new_nodes.append(node)
            continue
        
        for img in images:
            sections = remaining.split(f"![{img[0]}]({img[1]})", 1)
            remaining = sections[1]
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
        
        if len(remaining) != 0:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        remaining = node.text
        if len(links) == 0:
            new_nodes.append(node)
            continue
        
        for l in links:
            sections = remaining.split(f"[{l[0]}]({l[1]})", 1)
            remaining = sections[1]
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(l[0], TextType.LINK, l[1]))
        
        if len(remaining) != 0:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes