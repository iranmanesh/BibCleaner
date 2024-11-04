import re
import sys
from pathlib import Path

def extract_bib_keys(bib_file_path):
    """
    Extract all reference keys from a BibTeX file.
    Returns a set of keys in lowercase for case-insensitive comparison.
    """
    bib_keys = set()
    entry_types = r'@(?:article|misc|inbook|inproceedings|techreport|incollection)'
    
    with open(bib_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Remove comments
        content = re.sub(r'%.*$', '', content, flags=re.MULTILINE)
        
        # Find all BibTeX entries
        pattern = rf'{entry_types}\s*{{([^,]+),'
        matches = re.finditer(pattern, content, re.IGNORECASE)
        
        for match in matches:
            # Extract and clean the key
            key = match.group(1).strip()
            bib_keys.add(key.lower())
    
    return bib_keys

def extract_tex_citations(tex_file_path):
    """
    Extract all citation keys from a LaTeX file.
    Supports various citation commands including \\citet, \\citep, \\citet*, \\citep*,
    \\citeauthor, \\citeyear, and their variants.
    Returns a set of keys in lowercase for case-insensitive comparison.
    """
    tex_citations = set()
    
    # Define all possible citation commands
    cite_commands = [
        r'\\cite[tp]?\*?',     # \cite, \citep, \citet and their * variants
        r'\\citeauthor\*?',    # \citeauthor and \citeauthor*
        r'\\citeyear',         # \citeyear
        r'\\cite(?:alt|alp|num|text|url)',  # other common cite variants
    ]
    
    with open(tex_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Remove comments
        content = re.sub(r'%.*$', '', content, flags=re.MULTILINE)
        
        # Create pattern for all citation commands
        cite_pattern = r'(?:' + '|'.join(cite_commands) + r')\s*{([^}]+)}'
        matches = re.finditer(cite_pattern, content)
        
        for match in matches:
            # Handle multiple citations separated by comma
            citations = match.group(1).split(',')
            for citation in citations:
                # Clean the citation key (remove spaces and optional arguments)
                clean_citation = re.sub(r'\[.*?\]', '', citation)  # Remove optional arguments
                clean_citation = clean_citation.strip()
                if clean_citation:  # Only add non-empty citations
                    tex_citations.add(clean_citation.lower())
    
    return tex_citations

def find_unused_references(bib_file_path, tex_file_path):
    """
    Find references that are in the BibTeX file but not used in the LaTeX file.
    Prints detailed statistics about references usage.
    """
    try:
        # Get all references from both files
        bib_keys = extract_bib_keys(bib_file_path)
        tex_citations = extract_tex_citations(tex_file_path)
        
        # Find unused and used references
        unused_refs = bib_keys - tex_citations
        used_refs = bib_keys & tex_citations
        unknown_citations = tex_citations - bib_keys
        
        # Print results
        print("\n=== Reference Analysis Results ===")
        
        if unused_refs:
            print(f"\nUnused references ({len(unused_refs)}):")
            for ref in sorted(unused_refs):
                print(f"- {ref}")
        else:
            print("\nNo unused references found!")
            
        if unknown_citations:
            print(f"\nWarning: Citations not found in BibTeX file ({len(unknown_citations)}):")
            for ref in sorted(unknown_citations):
                print(f"- {ref}")
        
        # Print statistics
        print(f"\nStatistics:")
        print(f"- Total references in bib file: {len(bib_keys)}")
        print(f"- Total citations in tex file: {len(tex_citations)}")
        print(f"- Used references: {len(used_refs)}")
        print(f"- Unused references: {len(unused_refs)}")
        print(f"- Unknown citations: {len(unknown_citations)}")
        
    except FileNotFoundError as e:
        print(f"Error: Could not find file - {e.filename}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <bib_file> <tex_file>")
        sys.exit(1)
    
    bib_file = Path(sys.argv[1])
    tex_file = Path(sys.argv[2])
    
    find_unused_references(bib_file, tex_file)

if __name__ == "__main__":
    main()
