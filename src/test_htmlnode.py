import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        prop = {
                    "href": "https://www.google.com",
                    "target": "_blank",
                }
        
        node = HTMLNode(props=prop)
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")