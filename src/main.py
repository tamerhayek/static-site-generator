import os
from pathlib import Path
import shutil

from block_markdown import markdown_to_blocks, markdown_to_html_node
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
    )

def copy(src: str, dst: str):
	if not os.path.exists(src):
		raise ValueError(f"Source {src} does not exist")
	if os.path.exists(dst):
		shutil.rmtree(dst)
	os.mkdir(dst)

	for file in os.listdir(src):
		src_file = os.path.join(src, file)
		dst_file = os.path.join(dst, file)
		print(f" * {src_file} -> {dst_file}")
		if os.path.isdir(src_file):
			copy(src_file, dst_file)
		else:
			shutil.copy(src_file, dst_file)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

if __name__ == "__main__":
	main()