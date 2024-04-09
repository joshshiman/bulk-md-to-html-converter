# Bulk MD to HTML Converter

This script will recursively clone every markdown file and image in a directory and deposit all markdown files in a folder with a nestled images folder.

### Getting Started

To get started, ensure that you have Python3 and Git installed on your computer.

- `sudo install python3`
- `sudo install git-all`

Clone the repostiory by running this in the terminal

- `git clone https://github.com/joshshiman/bulk-md-to-html-converter.git`

Change directories to the project

- `cd bulk-md-to-html-converter`

Next install all dependencies

- `pip3 install -r requirements.txt`

### Running the Script

`python3 convert.py`

*Note: Currently you must remove `.md` files manually if you would not like to include them in the destination folder*