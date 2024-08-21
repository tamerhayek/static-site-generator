from htmlnode import HTMLNode


class ParentNode(HTMLNode):
	def __init__(self, tag: str, children: list, props: dict = None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if self.tag is None:
			raise ValueError("Invalid HTML: no tag")
		if self.children is None:
			raise ValueError("Invalid HTML: no children")

		node = ""
		if self.props is not None:
			node = f"<{self.tag} " + self.props_to_html() + ">"
		else:
			node = f"<{self.tag}>"

		for child in self.children:
			node += child.to_html()
		node += f"</{self.tag}>"
		return node

	def __repr__(self):
		return self.to_html()