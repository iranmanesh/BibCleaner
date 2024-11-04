# BibTeX Reference Checker

A Python script that helps you identify unused references in your LaTeX documents by comparing your BibTeX file against the citations in your LaTeX files. It supports a comprehensive range of citation commands and provides detailed analysis of reference usage.

## Features

- Identifies references that exist in your BibTeX file but aren't cited in your LaTeX document
- Detects citations in your LaTeX document that don't exist in your BibTeX file
- Supports multiple BibTeX entry types:
  - @article
  - @misc
  - @inbook
  - @inproceedings
  - @techreport
  - @incollection
- Handles all common LaTeX citation commands:
  - \cite{} - Basic citation
  - \citet{} - Textual citation
  - \citep{} - Parenthetical citation
  - \citet*{} - Textual citation with all author names
  - \citep*{} - Parenthetical citation with all author names
  - \citeauthor{} - Author names only
  - \citeyear{} - Year only
  - Other variants (citealt, citealp, citenum, citetext, citeurl)
- Case-insensitive comparison to avoid false positives
- Handles multiple citations within a single cite command
- Supports optional arguments in citation commands (e.g., \citep[see][p. 42]{reference})
- Ignores comments in both BibTeX and LaTeX files
- Provides comprehensive statistics about reference usage

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/bibtex-reference-checker.git
cd bibtex-reference-checker
```

2. Make the script executable (Unix-like systems):
```bash
chmod +x bib_checker.py
```

## Usage

Run the script from the command line by providing paths to your BibTeX and LaTeX files:

```bash
python bib_checker.py path/to/references.bib path/to/paper.tex
```

### Example Output

```
=== Reference Analysis Results ===

Unused references (3):
- smith2020
- jones2019
- wilson2021

Warning: Citations not found in BibTeX file (1):
- brown2022

Statistics:
- Total references in bib file: 45
- Total citations in tex file: 43
- Used references: 42
- Unused references: 3
- Unknown citations: 1
```

## Error Handling

The script handles several common errors:
- Missing input files
- File encoding issues
- Invalid file formats
- Malformed citation commands
- Citations with optional arguments

## Limitations

- Currently does not process nested LaTeX files (\input or \include)
- Does not validate BibTeX syntax
- Cannot process cite commands with complex optional arguments

[Rest of the README remains the same as before...]
