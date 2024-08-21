import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
	def test_to_html_no_tag(self):
		children = [LeafNode("p", "This is a html node")]
		node = ParentNode(None, children, None)
		self.assertRaises(ValueError, node.to_html)
	def test_to_html_no_children(self):
		node = ParentNode("div", None, None)
		self.assertRaises(ValueError, node.to_html)
	def test_to_html(self):
		children = [LeafNode("p", "This is a html paragraph"), LeafNode("a", "This is a html link", {"href": "https://tamerhayek.com", "target": "_blank"})]
		node = ParentNode("div", children, None)
		self.assertEqual(node.to_html(), "<div><p>This is a html paragraph</p><a href='https://tamerhayek.com' target='_blank'>This is a html link</a></div>")
	def test_to_html_props(self):
		children = [LeafNode("p", "This is a html paragraph"), LeafNode("a", "This is a html link", {"href": "https://tamerhayek.com", "target": "_blank"})]
		props = {
			"class": "bold"
		}
		node = ParentNode("div", children, props)
		self.assertEqual(node.to_html(), "<div class='bold'><p>This is a html paragraph</p><a href='https://tamerhayek.com' target='_blank'>This is a html link</a></div>")
	def test_repr(self):
		children = [LeafNode("p", "This is a html paragraph"), LeafNode("a", "This is a html link", {"href": "https://tamerhayek.com", "target": "_blank"})]
		props = {
			"class": "bold"
		}
		node = ParentNode("div", children, props)
		self.assertEqual(repr(node), "<div class='bold'><p>This is a html paragraph</p><a href='https://tamerhayek.com' target='_blank'>This is a html link</a></div>")


if __name__ == "__main__":
	unittest.main()