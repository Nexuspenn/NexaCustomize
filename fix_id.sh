#!/bin/bash

# Define the old and new strings
OLD="nexusfoundation.nexaos.customize"
NEW="org.nexuspenn.nexaos.customize"

echo "Replacing text inside files..."
# This finds all text files and replaces the ID string
grep -rl "$OLD" . --exclude="fix_id.sh" | xargs sed -i "s/$OLD/$NEW/g"

echo "Renaming files..."
# This finds files with the old name and renames them
find . -name "*$OLD*" | while read -r file; do
    new_file=$(echo "$file" | sed "s/$OLD/$NEW/")
    mkdir -p "$(dirname "$new_file")"
    mv "$file" "$new_file"
    echo "Renamed: $file -> $new_file"
done

echo "Done! Please check your git status to verify changes."
