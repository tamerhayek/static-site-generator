import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
	def test_eq(self):
		node = HTMLNode("p", "This is a html node")
		self.assertEqual(node.tag, "p")
		self.assertEqual(node.value, "This is a html node")
		self.assertEqual(node.children, None)
		self.assertEqual(node.props, None)
	def test_eq_children(self):
		childrens = [HTMLNode("b", "bold text")]
		node = HTMLNode("p", "This is a html node", childrens)
		self.assertEqual(node.tag, "p")
		self.assertEqual(node.value, "This is a html node")
		self.assertEqual(node.children, childrens)
		self.assertEqual(node.props, None)
	def test_eq_props(self):
		props = {"class": "bold"}
		node = HTMLNode("p", "This is a html node", props=props)
		self.assertEqual(node.tag, "p")
		self.assertEqual(node.value, "This is a html node")
		self.assertEqual(node.children, None)
		self.assertEqual(node.props, props)
	def test_to_html(self):
		node = HTMLNode("p", "This is a html node")
		self.assertRaises(NotImplementedError, node.to_html)
	def test_props_to_html(self):
		props = {"href": "https://tamerhayek.com", "class": "bold", "target": "_blank"}
		node = HTMLNode("a", "This is a html node", props=props)
		self.assertEqual(node.props_to_html(), "href='https://tamerhayek.com' class='bold' target='_blank'")
	def test_repr(self):
		childrens = [HTMLNode("b", "bold text")]
		props = {"class": "bold"}
		node = HTMLNode("p", "This is a html node", childrens, props)
		self.assertEqual(repr(node), "HTMLNode(p, This is a html node, [HTMLNode(b, bold text, None, None)], {'class': 'bold'})")

if __name__ == "__main__":
	unittest.main()