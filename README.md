# Process Text to Markdown

## Overview

This Python script converts text files (`.txt`) into well-formatted Markdown files (`.md`). It normalizes line endings, replaces problematic characters, and beautifies the Markdown output to ensure readability and consistency. The script supports batch processing of files in a directory as well as single-file processing.

## Features

- Normalizes line endings to LF.
- Replaces problematic characters (e.g., Windows-1252 right single quotation mark).
- Beautifies Markdown output by removing excessive line breaks, formatting long lines, and adding emphasis to uppercase phrases.
- Supports processing of both single files and multiple files in a directory.
- Outputs processed files with a `_processed` suffix by default.

## Installation

Ensure you have Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/).

## Usage

1. **Run the script**:

```sh
python process_to_markdown.py
```

2. **Choose Processing Mode**:
- **Process Directory**: Select a directory containing `.txt` or `.md` files to process. Specify an output directory where the converted files will be saved.
- **Process Single File**: Select a single `.txt` or `.md` file to process. Choose the output file location for the converted Markdown file.

3. **Processing Options**:
- Files are processed to replace problematic characters and beautify Markdown.
- Processed files are saved with a `_processed` suffix by default.

---

Thank you for using Useful-Tools!