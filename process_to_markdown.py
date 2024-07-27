import tkinter as tk
from tkinter import filedialog
import os
import re

def process_text_file_to_markdown(input_file, output_file):
    content = read_file_with_fallback(input_file)
    
    # Normalize line endings to LF
    content = content.replace('\r\n', '\n').replace('\r', '\n')

    # Replace problematic characters
    content = replace_problematic_characters(content)

    # Split content into lines
    lines = content.split('\n')

    # Process lines to remove single line breaks but preserve double line breaks and handle multiple new lines
    processed_lines = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == '':
            # Check for consecutive empty lines
            if i > 0 and lines[i-1].strip() == '':
                # Skip additional empty lines
                while i < len(lines) and lines[i].strip() == '':
                    i += 1
                processed_lines.append('')
            else:
                i += 1
        else:
            current_line = lines[i].strip()
            while (i + 1 < len(lines)) and lines[i + 1].strip() != '':
                current_line += ' ' + lines[i + 1].strip()
                i += 1
            processed_lines.append(current_line)
            i += 1

    # Join processed lines with double new lines
    result = '\n\n'.join(processed_lines)

    # Beautify Markdown output
    result = beautify_markdown(result)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result)

def read_file_with_fallback(file_path):
    encodings = ['utf-8', 'latin-1', 'windows-1252']  # List of encodings to try
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc, errors='replace') as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Unable to decode file with available encodings: {file_path}")

def replace_problematic_characters(text):
    # Direct replacement for problematic characters
    replacements = {
        '\x92': "'"  # Windows-1252 right single quotation mark
    }
    
    for key, value in replacements.items():
        text = text.replace(key, value)
    
    return text

def beautify_markdown(text):
    # Convert multiple new lines to a single paragraph break
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Format long lines
    lines = text.split('\n')
    formatted_lines = []
    for line in lines:
        while len(line) > 80:
            # Find last space within the limit
            split_index = line.rfind(' ', 0, 80)
            if split_index == -1:
                split_index = 80
            formatted_lines.append(line[:split_index])
            line = line[split_index:].lstrip()
        formatted_lines.append(line)
    
    # Join lines with new line
    text = '\n'.join(formatted_lines)

    # Add emphasis and headers (example - customize based on patterns)
    text = re.sub(r'\b([A-Z][A-Z\s]+[A-Z])\b', r'**\1**', text)  # Bold uppercase phrases

    return text

def process_files_in_directory(directory, output_directory):
    supported_extensions = ('.txt', '.md')

    for filename in os.listdir(directory):
        if filename.lower().endswith(supported_extensions):
            input_file = os.path.join(directory, filename)
            base_name, ext = os.path.splitext(filename)
            output_file = os.path.join(output_directory, f'{base_name}_processed{ext}')
            process_text_file_to_markdown(input_file, output_file)
            print(f"Processed file saved as: {output_file}")

def choose_mode():
    def on_directory_mode():
        root.quit()
        process_directory()

    def on_single_file_mode():
        root.quit()
        process_single_file()

    root = tk.Tk()
    root.title("Choose Mode")
    root.geometry("300x150")

    tk.Label(root, text="Choose processing mode:", padx=20, pady=10).pack()
    
    tk.Button(root, text="Process Directory", command=on_directory_mode, padx=20, pady=5).pack()
    tk.Button(root, text="Process Single File", command=on_single_file_mode, padx=20, pady=5).pack()

    root.mainloop()

def process_directory():
    directory = filedialog.askdirectory(title="Select Directory with Text or Markdown Files")
    if not directory:
        print("No directory selected. Exiting...")
        return
    output_directory = filedialog.askdirectory(title="Select Output Directory")
    if not output_directory:
        print("No output directory selected. Exiting...")
        return
    process_files_in_directory(directory, output_directory)

def process_single_file():
    input_file = filedialog.askopenfilename(title="Select a text or Markdown file", filetypes=[("Text files", "*.txt"), ("Markdown files", "*.md")])
    if not input_file:
        print("No file selected. Exiting...")
        return

    output_file = filedialog.asksaveasfilename(title="Save as Markdown", defaultextension=".md", filetypes=[("Markdown files", "*.md")])
    if not output_file:
        print("No output file selected. Exiting...")
        return

    process_text_file_to_markdown(input_file, output_file)
    print(f"Processed file saved as: {output_file}")

if __name__ == "__main__":
    choose_mode()