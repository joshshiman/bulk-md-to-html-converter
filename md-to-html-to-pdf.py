import os
import shutil
import markdown2
from xhtml2pdf import pisa

def clone_md_and_images(src_dir, dest_dir):
    # Create the destination 'images' directory if it doesn't exist
    dest_images_dir = os.path.join(dest_dir, 'images')
    os.makedirs(dest_images_dir, exist_ok=True)

    # Walk through the source directory
    for root, dirs, files in os.walk(src_dir):
        # Check if there is an 'images' directory in the current directory
        if 'images' in dirs:
            images_dir = os.path.join(root, 'images')
            # Copy all images from the 'images' directory to the destination 'images' directory
            for file in os.listdir(images_dir):
                src_img_path = os.path.join(images_dir, file)
                if os.path.isfile(src_img_path):
                    dest_img_path = os.path.join(dest_images_dir, file)
                    shutil.copy2(src_img_path, dest_img_path)

        # Copy markdown files to the destination directory
        for file in files:
            if file.endswith('.md'):
                src_md_path = os.path.join(root, file)
                dest_md_path = os.path.join(dest_dir, file)
                shutil.copy2(src_md_path, dest_md_path)

def convert_md_to_html(dest_dir):
    # Convert markdown files to HTML
    for root, _, files in os.walk(dest_dir):
        for file in files:
            if file.endswith('.md'):
                src_md_path = os.path.join(root, file)
                dest_html_path = os.path.join(root, os.path.splitext(file)[0] + '.html')
                with open(src_md_path, 'r') as md_file:
                    md_content = md_file.read()

                    # Convert Markdown to HTML with improved table rendering
                    html_content = markdown2.markdown(md_content, extras=["tables"])

                    # Replace image paths with absolute paths
                    html_content = html_content.replace('src="images/', f'src="{os.path.abspath(os.path.join(dest_dir, "images/"))}/')

                    with open(dest_html_path, 'w') as html_file:
                        html_file.write(html_content)

def convert_html_to_pdf(dest_dir):
    # Convert HTML files to PDF using xhtml2pdf
    for root, _, files in os.walk(dest_dir):
        for file in files:
            if file.endswith('.html'):
                src_html_path = os.path.join(root, file)
                dest_pdf_path = os.path.join(root, os.path.splitext(file)[0] + '.pdf')
                
                with open(src_html_path, 'r') as html_file:
                    html_content = html_file.read()

                with open(dest_pdf_path, 'wb') as pdf_file:
                    pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)

                # Check if the PDF was successfully created
                if pisa_status.err:
                    print(f"Failed to create {dest_pdf_path}")
                else:
                    print(f"Successfully created {dest_pdf_path}")

def main():
    # Path to the source directory
    src_dir = 'your directory here'

    # Path to the destination directory
    dest_dir = 'your directory here'

    # Clone markdown files and images
    clone_md_and_images(src_dir, dest_dir)

    # Convert markdown files to HTML
    convert_md_to_html(dest_dir)

    # Convert HTML files to PDF
    convert_html_to_pdf(dest_dir)

if __name__ == "__main__":
    main()
