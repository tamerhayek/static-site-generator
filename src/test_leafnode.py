import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
	def test_eq(self):
		node = LeafNode("p", "This is a html node")
		self.assertEqual(node.tag, "p")
		self.assertEqual(node.value, "This is a html node")
		self.assertEqual(node.children, None)
		self.assertEqual(node.props, None)
	def test_eq_props(self):
		props = {"class": "bold"}
		node = LeafNode("p", "This is a html node", props=props)
		self.assertEqual(node.tag, "p")
		self.assertEqual(node.value, "This is a html node")
		self.assertEqual(node.children, None)
		self.assertEqual(node.props, props)
	def test_to_html_value(self):
		node = LeafNode("p", "This is a html node")
		self.assertEqual(repr(node), "<p>This is a html node</p>")
	def test_to_html_no_value(self):
		node = LeafNode("p")
		self.assertRaises(ValueError, node.to_html)
	def test_to_html_no_tag(self):
		node = LeafNode(None, "This is a html node")
		self.assertEqual(repr(node), "This is a html node")
	def test_to_html_props(self):
		props = {
			"href": "https://www.boot.dev",
			"target": "_blank",
			"class": "bold"
		}
		node = LeafNode("a", "This is a html node", props)
		self.assertEqual(repr(node), "<a href='https://www.boot.dev' target='_blank' class='bold'>This is a html node</a>")
	def test_repr(self):
		props = {"class": "bold"}
		node = LeafNode("p", "This is a html node", props)
		self.assertEqual(repr(node), "<p class='bold'>This is a html node</p>")


if __name__ == "__main__":
	unittest.main()