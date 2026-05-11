import unittest

from markdown_blocks import *

class TestMarkdownBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_heading(self):
            block = "## Hello"
            self.assertEqual(block_to_block_type(block), BlockType.heading)

        def test_code(self):
            block = "```\nHello\n```"
            self.assertEqual(block_to_block_type(block), BlockType.code)

        def test_quote(self):
            block = "> Hello`"
            self.assertEqual(block_to_block_type(block), BlockType.quote)

        def test_ul(self):
            block = "- Hello "
            self.assertEqual(block_to_block_type(block), BlockType.unordered_list)

        def test_ol(self):
            block = "1. Hello"
            self.assertEqual(block_to_block_type(block), BlockType.ordered_list)

if __name__ == 'main':
    unittest.main()