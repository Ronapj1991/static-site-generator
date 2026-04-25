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
