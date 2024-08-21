import os
import shutil

from block_markdown import markdown_to_blocks, markdown_to_html_node

def main():
	copy("./static", "./public")
	generate_page("./content/index.md", "./template.html", "./public/index.html")

def copy(src: str, dst: str):
	if not os.path.exists(src):
		raise ValueError(f"Source {src} does not exist")
	if os.path.exists(dst):
		shutil.rmtree(dst)
	os.mkdir(dst)

	for file in os.listdir(src):
		src_file = os.path.join(src, file)
		dst_file = os.path.join(dst, file)
		if os.path.isdir(src_file):
			copy(src_file, dst_file)
		else:
			shutil.copy(src_file, dst_file)

def extract_title(markdown: str):
	blocks = markdown_to_blocks(markdown)
	for block in blocks:
		if block.startswith("# "):
			return block.replace("# ", "")
	raise ValueError("No title found")

def generate_page(from_path: str, template_path: str, dest_path: str):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	from_path_content = open(from_path, "r").read()
	template_path_content = open(template_path, "r").read()

	from_path_html = markdown_to_html_node(from_path_content).to_html()
	from_path_title = extract_title(from_path_content)

	html = template_path_content.replace("{{ Title }}", from_path_title).replace("{{ Content }}", from_path_html)

	open(dest_path, "w").write(html)

if __name__ == "__main__":
	main()