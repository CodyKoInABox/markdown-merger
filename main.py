# python main.py <input_folder> <output_folder>
# python main.py ./docs ./output

import os
import sys
from pathlib import Path

def merge_markdown_files(input_folder, output_folder):
    """
    Merge all .md and .mdx files from input_folder into one big file in output_folder
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    
    # Validate input folder exists
    if not input_path.exists():
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return False
    
    # Create output folder if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all .md and .mdx files in input folder
    md_files = list(input_path.glob("*.md"))
    mdx_files = list(input_path.glob("*.mdx"))
    all_files = md_files + mdx_files
    
    if not all_files:
        print(f"No .md or .mdx files found in '{input_folder}'")
        return False
    
    # Sort files for consistent ordering
    all_files.sort()
    
    # Output file path
    merged_file = output_path / "merged_markdown.md"
    
    print(f"Found {len(all_files)} markdown files to merge:")
    for file in all_files:
        print(f"  - {file.name}")
    
    # Merge all files
    with open(merged_file, 'w', encoding='utf-8') as outfile:
        for i, md_file in enumerate(all_files):
            # Add separator between files (except for the first one)
            if i > 0:
                outfile.write("\n\n" + "="*80 + "\n\n")
            
            # Add file header
            outfile.write(f"# Content from: {md_file.name}\n\n")
            
            try:
                with open(md_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    
                    # Ensure content ends with newline
                    if content and not content.endswith('\n'):
                        outfile.write('\n')
                        
            except Exception as e:
                print(f"Warning: Could not read file '{md_file.name}': {e}")
                outfile.write(f"*Error reading file: {e}*\n\n")
    
    print(f"\nMerged file created: {merged_file}")
    return True

def main():
    if len(sys.argv) != 3:
        print("Usage: python merge_markdown.py <input_folder> <output_folder>")
        print("\nExample:")
        print("  python merge_markdown.py ./docs ./output")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    print("-" * 50)
    
    success = merge_markdown_files(input_folder, output_folder)
    
    if success:
        print("\nMerge completed successfully!")
    else:
        print("\nMerge failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()