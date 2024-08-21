class HTMLNode:
	def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("to_html is not implemented")

	def props_to_html(self) -> str:
		texts = []
		for key, value in self.props.items():
			texts.append(f"{key}='{value}'")
		return " ".join(texts)

	def __repr__(self) -> str:
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"