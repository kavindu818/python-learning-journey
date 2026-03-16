# Day 6: Python File Handling
print("=== File Handling Basics ===")

"""
There are has 3 main modes:

    1. w (Write): Creates a new file. If there is an old one, it is deleted and a new one is written.

    2. a (Append): Appends the old file without deleting it, and adds new content to it.

    3. r (Read): Reads the content of the file.

"""

# 1. Creating a new file and writing to it ("w" - Write mode)

my_file = open("freelance_notes.txt", "w")
my_file.write("My first saved note!\n")
my_file.write("Focusing 100% on Software Engineering.\n")
my_file.close()
print("Data successfully Saved to the hard disk!\n")

# 2. Reading a file on the hard disk ("r" - Read mode)

print("--- Reading the saved data ---")
read_file = open("freelance_notes.txt", "r")
saved_content = read_file.read()
print(saved_content)
read_file.close()

# 3. Append (adding new things without deleting old ones)

append_file = open("freelance_notes.txt", "a")
append_file.write("Learning file handling is awesome!\n")
append_file.close()

# Note: We don't need to use different variables like my_file, read_file, and append_file to open the same file.
#       I used different names like my_file, append_file, and read_file to avoid confusion when learning at first.
#       When coding as an Industry Standard (real world) we don't use different names. Most people just use the variable name 'file' or 'f'.
