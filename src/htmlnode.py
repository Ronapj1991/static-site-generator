
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented")

    def props_to_html(self):
        if self.props == None:
            return ""
        
        res = ""
        for tag, value in self.props.items():
            res += f" {tag}=\"{value}\""
        return res

    def __repr__(self):
        return f"Tag:{self.tag}, Value:{self.value}, Children: {self.children} \nProperties:{self.props}"