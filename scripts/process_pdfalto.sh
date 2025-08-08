#!/bin/bash

# Function to process PDF files
process_pdf_files() {
  local input_dir="$1"
  local output_dir="$2"
  local pdfalto_path="$3"

  # Create the output directory if it doesn't exist
  mkdir -p "$output_dir"

  # Loop through all files and directories in the input directory
  for entry in "$input_dir"/*; do
    if [ -d "$entry" ]; then
      # If the entry is a directory, recursively process it
      local subdir_name=$(basename "$entry")
      process_pdf_files "$entry" "$output_dir/$subdir_name" "$pdfalto_path"
    elif [ -f "$entry" ] && [[ "$entry" == *.pdf ]]; then
      # If the entry is a PDF file, process it with pdfalto
      echo "Processing $entry"
      local filename=$(basename "$entry")
      ${pdfalto_path}/./pdfalto -noImageInline -fullFontName -noImage -readingOrder "$entry" "$output_dir/${filename%.pdf}.xml"
    fi
  done
}

# Main script execution
input_directory="$1"
output_directory="$2"
pdfalto_path="$3"

if [ -z "$input_directory" ] || [ -z "$output_directory" ] || [ -z "$pdfalto_path" ]; then
  echo "Usage: $0 <input_directory> <output_directory> <pdfalto_absolute_path>"
  exit 1
fi

process_pdf_files "$input_directory" "$output_directory" "$pdfalto_path"
