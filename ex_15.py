from sys import argv

script, filename = argv
prompt = "> "
txt = open(filename)


print("Here's your file: %s" % filename)
print(txt.read())

print("Type the filename again please")
filename = input(prompt)

print("Here's your file (again): %s" % filename)
txt = open(filename)
print(txt.read())
