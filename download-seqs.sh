#!/bin/bash

# File containing the list of URLs
url_file=$1

# Loop through each URL in the file
while IFS= read -r url; do
    file_name=$(basename "$url")
    echo "Downloading $file_name..."
    wget "$url" -O "$file_name"
    
    # Check if the file was downloaded successfully
    if [ $? -eq 0 ]; then
        echo "Successfully downloaded $file_name"
        gunzip "$file_name"
        echo "Extracted $file_name"
    else
        echo "Failed to download $file_name"
    fi
done < "$url_file"

echo "All downloads complete."
