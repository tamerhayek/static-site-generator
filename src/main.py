import os
import shutil

from block_markdown import markdown_to_blocks

def main():
	copy("./static", "./public")

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

if __name__ == "__main__":
	main()