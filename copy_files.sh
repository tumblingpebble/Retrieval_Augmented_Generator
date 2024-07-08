#!/bin/bash

# Source directory
SOURCE_DIR="/home/tumblingpebble/download/langchain-api"

# Target directory
TARGET_DIR="/home/tumblingpebble/download/agentai/copied_files"

# Create the target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Read the file list and copy each file to the target directory
while IFS= read -r file; do
  echo "Searching for file: $file"
  # Find files matching the current filename (ignoring extensions) within subdirectories
  found_files=$(find "$SOURCE_DIR" -type f -name "$(basename "$file")*")
  if [ -z "$found_files" ]; then
    echo "No files found for: $file"
  else
    echo "Found files for: $file"
    echo "$found_files"
    # Copy each found file to the target directory
    while IFS= read -r found_file; do
      echo "Copying $found_file to $TARGET_DIR"
      cp "$found_file" "$TARGET_DIR"
    done <<< "$found_files"
  fi
done < file_list.txt

echo "All specified files have been copied to $TARGET_DIR"
