def add(a, b):
    print("Adding %d and %d" % (a, b))
    return a+b

def subtract(a, b):
    print("subtracting %d and %d" % (a, b))
    return a-b

def multiply(a, b):
    print("Multiplying %d and %d" % (a, b))
    return a*b

def divide(a, b):
    print("Dividing %d and %d" % (a, b))
    return a/b

age = add(30, 5)
height = subtract(23, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

