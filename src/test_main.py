import unittest

from main import extract_title

class TestMain(unittest.TestCase):
	def test_extract_title(self):
		markdown = "# Hello"
		title = extract_title(markdown)
		self.assertEqual(title, "Hello")

	def test_extract_title_long_markdown(self):
		markdown = """
# Hello

This is a long title

This is another paragraph

This is the end
		"""
		title = extract_title(markdown)
		self.assertEqual(title, "Hello")

	def test_extract_no_title(self):
		markdown = "## Hello"
		self.assertRaises(ValueError, extract_title, markdown)

if __name__ == "__main__":
	unittest.main()