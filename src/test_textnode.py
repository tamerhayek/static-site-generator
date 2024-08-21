import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node", "bold")
		self.assertEqual(node, node2)
	def test_not_eq_text(self):
		node = TextNode("This is a text node 1", "bold")
		node2 = TextNode("This is a text node 2", "bold")
		self.assertNotEqual(node, node2)
	def test_not_eq_text_type(self):
		node = TextNode("This is a text node", "italic")
		node2 = TextNode("This is a text node", "bold")
		self.assertNotEqual(node, node2)
	def test_not_eq_url(self):
		node = TextNode("This is a text node", "bold", "https://www.boot.dev")
		node2 = TextNode("This is a text node", "bold")
		self.assertNotEqual(node, node2)
	def test_repr(self):
		node = TextNode("This is a text node", "bold", "https://www.boot.dev")
		self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://www.boot.dev)")

	def test_text_node_to_html_node(self):
		node = TextNode("This is a text node", TextType.TEXT)
		leaf = LeafNode(None, "This is a text node")
		self.assertEqual(repr(text_node_to_html_node(node)), repr(leaf))
	def test_text_node_to_html_node_bold(self):
		node = TextNode("This is a bold tag", TextType.BOLD)
		leaf = LeafNode("b", "This is a bold tag")
		self.assertEqual(repr(text_node_to_html_node(node)), repr(leaf))
	def test_text_node_to_html_node_italic(self):
		node = TextNode("This is a italic tag", TextType.ITALIC)
		leaf = LeafNode("i", "This is a italic tag")
		self.assertEqual(repr(text_node_to_html_node(node)), repr(leaf))
	def test_text_node_to_html_node_code(self):
		node = TextNode("This is a code tag", TextType.CODE)
		leaf = LeafNode("code", "This is a code tag")
		self.assertEqual(repr(text_node_to_html_node(node)), repr(leaf))
	def test_text_node_to_html_node_link(self):
		node = TextNode("This is a link tag", TextType.LINK, "https://tamerhayek.com")
		leaf = LeafNode("a", "This is a link tag", {"href": "https://tamerhayek.com" })
		self.assertEqual(repr(text_node_to_html_node(node)), repr(leaf))
	def test_text_node_to_html_node_link(self):
		node = TextNode("This is a image tag", TextType.IMAGE, "https://tamerhayek.com/avatar.webp")
		leaf = LeafNode("img", "", {"src": "https://tamerhayek.com/avatar.webp", "alt": "This is a image tag" })
		self.assertEqual(repr(text_node_to_html_node(node)), repr(leaf))
	def test_text_node_to_html_node_default(self):
		node = TextNode("This is a default fallback", "")
		self.assertRaises(ValueError, text_node_to_html_node, node)


if __name__ == "__main__":
	unittest.main()