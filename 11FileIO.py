# FileIO.py
#
# File input/output lets programs save data and read it later.
# pathlib helps us work with file paths in a clean, modern way.

from pathlib import Path

notes_path = Path("example_notes.txt")

# Write text to a file. This creates the file if it does not exist.
notes_path.write_text("Python is fun!\nFiles can store program data.\n")
print("Wrote notes to", notes_path)

# Read all text from the file.
notes = notes_path.read_text()
print("\nAll notes:")
print(notes)

# Read the file as separate lines.
print("Each note:")
for line_number, line in enumerate(notes.splitlines(), start=1):
    print(line_number, line)

# Add another line by reading the current text and writing updated text.
notes_path.write_text(notes + "Practice makes progress.\n")
print("\nUpdated notes:")
print(notes_path.read_text())
