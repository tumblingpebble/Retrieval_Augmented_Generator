#!/bin/bash

# Source directory
SOURCE_DIR="/home/tumblingpebble/download/langchain-api"

# Destination directory
DEST_DIR="/home/tumblingpebble/download/agentai/data"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Navigate to the source directory
cd "$SOURCE_DIR" || exit

# Find and copy all Markdown files, preserving the directory structure
find . -type f -name "*.md" -exec cp {} "$DEST_DIR" \;

echo "All Markdown files have been copied to $DEST_DIR"