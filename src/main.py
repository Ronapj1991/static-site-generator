from textnode import TextNode, TextType

def main():
    my_text = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(my_text)

main()