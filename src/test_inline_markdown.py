import unittest

from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
	def test_delim_bold(self):
		node = TextNode("This is text with a **bolded** word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded", TextType.BOLD),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

	def test_delim_bold_double(self):
		node = TextNode(
			"This is text with a **bolded** word and **another**", TextType.TEXT
		)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded", TextType.BOLD),
				TextNode(" word and ", TextType.TEXT),
				TextNode("another", TextType.BOLD),
			],
			new_nodes,
		)

	def test_delim_bold_multiword(self):
		node = TextNode(
			"This is text with a **bolded word** and **another**", TextType.TEXT
		)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded word", TextType.BOLD),
				TextNode(" and ", TextType.TEXT),
				TextNode("another", TextType.BOLD),
			],
			new_nodes,
		)

	def test_delim_italic(self):
		node = TextNode("This is text with an *italic* word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

	def test_delim_bold_and_italic(self):
		node = TextNode("**bold** and *italic*", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
		self.assertListEqual(
			[
				TextNode("bold", TextType.BOLD),
				TextNode(" and ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
			],
			new_nodes,
		)

	def test_delim_code(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

	def test_split_image(self):
		node = TextNode(
			"This is text with an ![image](https://tamerhayek.com/avatar.webp)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://tamerhayek.com/avatar.webp"),
			],
			new_nodes,
		)

	def test_split_image_single(self):
		node = TextNode(
			"![image](https://tamerhayek.com/avatar.webp)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("image", TextType.IMAGE, "https://tamerhayek.com/avatar.webp"),
			],
			new_nodes,
		)

	def test_split_images(self):
		node = TextNode(
			"This is text with an ![image](https://tamerhayek.com/avatar.webp) and another ![second image](https://tamerhayek.com/assets/images/portrait.webp)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://tamerhayek.com/avatar.webp"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
					"second image", TextType.IMAGE, "https://tamerhayek.com/assets/images/portrait.webp"
				),
			],
			new_nodes,
		)

	def test_split_no_image(self):
		node = TextNode(
			"This is a text with no image",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is a text with no image", TextType.TEXT),
			],
			new_nodes,
		)

	def test_split_link(self):
		node = TextNode(
			"This is text with a [link](https://tamerhayek.com)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://tamerhayek.com"),
			],
			new_nodes,
		)

	def test_split_link_single(self):
		node = TextNode(
			"[link](https://tamerhayek.com)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("link", TextType.LINK, "https://tamerhayek.com"),
			],
			new_nodes,
		)

	def test_split_links(self):
		node = TextNode(
			"This is text with a [link](https://tamerhayek.com) and [another link](https://tamerhayek.com/github) with text that follows",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://tamerhayek.com"),
				TextNode(" and ", TextType.TEXT),
				TextNode("another link", TextType.LINK, "https://tamerhayek.com/github"),
				TextNode(" with text that follows", TextType.TEXT),
			],
			new_nodes,
		)

	def test_split_no_link(self):
		node = TextNode(
			"This is a text with no link",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is a text with no link", TextType.TEXT),
			],
			new_nodes,
		)

	def test_extract_markdown_links(self):
		text = "This is text with a link [to tamerhayek.com](https://tamerhayek.com) and [to github](https://tamerhayek.com/github)"
		self.assertEqual(
			[
				("to tamerhayek.com", "https://tamerhayek.com"),
				("to github", "https://tamerhayek.com/github")
			],
			(extract_markdown_links(text))
		)

	def test_extract_markdown_links_no_links(self):
		text = "This is text with no links"
		self.assertEqual([], extract_markdown_links(text))

	def test_extract_markdown_images(self):
		text = "This is text with an image of ![Tamer Hayek](https://tamerhayek.com/avatar.webp)"
		self.assertEqual(
			[
				("Tamer Hayek", "https://tamerhayek.com/avatar.webp")
			],
			(extract_markdown_images(text))
		)

	def test_extract_markdown_images_no_images(self):
		text = "This is text with no images"
		self.assertEqual([], extract_markdown_images(text))

	def test_text_to_textnodes(self):
		nodes = text_to_textnodes("This is **bold** text with an *italic* word and a `code block` and an ![image](https://tamerhayek.com/avatar.webp) and a [link](https://tamerhayek.com)")

		self.assertEqual(
			nodes,
			[
				TextNode("This is ", TextType.TEXT, None),
				TextNode("bold", TextType.BOLD, None),
				TextNode(" text with an ", TextType.TEXT, None),
				TextNode("italic", TextType.ITALIC, None),
				TextNode(" word and a ", TextType.TEXT, None),
				TextNode("code block", TextType.CODE, None),
				TextNode(" and an ", TextType.TEXT, None),
				TextNode("image", TextType.IMAGE, "https://tamerhayek.com/avatar.webp"),
				TextNode(" and a ", TextType.TEXT, None),
				TextNode("link", TextType.LINK, "https://tamerhayek.com"),
			]
		)


if __name__ == "__main__":
	unittest.main()
