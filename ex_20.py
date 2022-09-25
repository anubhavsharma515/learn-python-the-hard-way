from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

# once you read the entire file from print_all(),
# the marker is at the end of the file.
# The rewind function sets the marker to beginning
# of the file.

def rewind(f):
    f.seek(0)

# How does readline() know where each line is?
# Inside readline() is code that scans each byte of the fi le until it fi nds a \n character, then stops 
# reading the fi le to return what it found so far. The fi le f is responsible for maintaining the current 
# position in the fi le after each readline() call, so that it will keep reading each line
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First we print the whole file")
print_all(current_file)

print("Now let's rewind, kinda like a tape")
rewind(current_file)

print("Let's print three lines")

for current_line in range(1, 4):
    print_a_line(current_line, current_file)
