from htmlnode import HTMLNode


class LeafNode(HTMLNode):
	def __init__(self, tag: str, value: str, props: dict = None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("Invalid HTML: no value")
		if self.tag is None:
			return self.value
		elif self.props is not None:
			return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
		else:
			return f"<{self.tag}>{self.value}</{self.tag}>"

	def __repr__(self):
		return self.to_html()