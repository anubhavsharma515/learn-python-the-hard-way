ten_things = "Apples Oranges Crows Telephone Light Sugar"

print(ten_things)
print("Wait there's not ten things in that list")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %s items now." % len(stuff))

print("There we go:", stuff)

print("Let's do some stuff with stuff (haha)")

print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

