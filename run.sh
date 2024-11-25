#!/bin/bash

# Set the directory to move PNG files to
DEST_DIR="/Users/chenfei/PHYS235W/Term-Paper/figure"

# Run all Python files in the current directory
for py_file in *.py; do
    # Check if any Python files exist
    if [ -f "$py_file" ]; then
        echo "Running $py_file..."
        python3 "$py_file"
    fi
done

# Move all PNG files generated in the current directory to the destination directory
for png_file in *.png; do
    # Check if any PNG files exist
    if [ -f "$png_file" ]; then
        echo "Moving $png_file to $DEST_DIR"
        mv "$png_file" "$DEST_DIR"
    fi
done

echo "All Python files executed, and PNG files moved to $DEST_DIR."
