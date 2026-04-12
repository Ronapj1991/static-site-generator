from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node needs a tag")
        if self.children is None:
            raise ValueError("Parent node needs a child")
        
        res = ""
        
        for child in self.children:
            res += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{res}</{self.tag}>"