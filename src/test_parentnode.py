import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode(None, [child_node])
            parent_node.to_html()

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", None)
            parent_node.to_html()

    def test_to_html_multiple_children(self):
        child1 = LeafNode("span", "child")
        child2 = LeafNode("b", "two")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>two</b></div>")

    def test_to_html_nested_parent(self):
        child = LeafNode("span", "child")
        parent1 = ParentNode("div", [child])
        parent2 = ParentNode("div", [parent1])
        self.assertEqual(parent2.to_html(), "<div><div><span>child</span></div></div>")

    def test_to_html_with_props(self):
        child = LeafNode("span", "child")
        parent_node = ParentNode("div", [child], {"class": "box"})
        self.assertEqual(parent_node.to_html(), "<div class=\"box\"><span>child</span></div>")

    def test_to_html_with_plaintext_child(self):
        child = LeafNode(None, "hello")
        child2 = LeafNode("b", "world")
        parent_node = ParentNode("p", [child, child2])
        self.assertEqual(parent_node.to_html(), "<p>hello<b>world</b></p>")