# This code sanitizes the followers txt file.
# Then we can use that sanitized txt file as input into 'follow_followers.py'

import re

# Read the text file. Write your output from 'extract_followers.py'
with open("ma.tempo.txt", "r") as file:
    data = file.readlines()

# Initialize a list to store unique lines
unique_lines = []

# Use regular expressions to extract the desired lines
for line in data:
    match = re.match(r"\d+ -> (.+)", line)
    if match:
        line_text = match.group(1)
        # Check if the line has already been encountered
        if line_text not in unique_lines:
            unique_lines.append(line_text)

# Write the sanitized lines. Write the custom name.
with open("sanitized_ma.tempo.txt", "w") as file:
    for line in unique_lines:
        file.write(line + "\n")
