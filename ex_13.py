# argv = arg[ument]v[ariable]
# This holds the arguments that you pass to
# your python script when you run it.

from sys import argv

# Unpacking the variables
script, first, second, third = argv

print("Script is called", script)
print("First variable is", first)
print("Second variable is", second)
print("Third variable is", third)
