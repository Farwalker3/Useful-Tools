#!/usr/bin/env python3

import re
import tkinter as tk
from tkinter import filedialog

def process_text_file_to_markdown(input_file, output_file):
	with open(input_file, 'r', encoding='utf-8') as file:
		content = file.read()
		
	# Step 1: Replace double line breaks with a unique marker
	content = content.replace('\n\n', '__DOUBLE_NEWLINE__')
	
	# Step 2: Replace single line breaks with a space
	content = content.replace('\n', ' ')
	
	# Step 3: Restore the double line breaks
	content = content.replace('__DOUBLE_NEWLINE__', '\n\n')
	
	with open(output_file, 'w', encoding='utf-8') as file:
		file.write(content)
		
def main():
	root = tk.Tk()
	root.withdraw()  # Hide the root window
	
	# Prompt the user to select a file
	input_file = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
	if not input_file:
		print("No file selected. Exiting...")
		return
	
	# Let the user select the output file location and name
	output_file = filedialog.asksaveasfilename(title="Save as Markdown", defaultextension=".md", filetypes=[("Markdown files", "*.md")])
	if not output_file:
		print("No output file selected. Exiting...")
		return
	
	process_text_file_to_markdown(input_file, output_file)
	print(f"Processed file saved as: {output_file}")
	
if __name__ == "__main__":
	main()