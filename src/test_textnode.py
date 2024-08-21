import unittest

from textnode import TextNode


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


if __name__ == "__main__":
	unittest.main()