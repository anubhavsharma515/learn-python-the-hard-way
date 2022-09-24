num_people_types = 10
x = "There are %d types of people." % num_people_types

binary = "binary"
do_not = "don't"

y = "Those who know %s and thos who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: %r." % y)

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

print(joke_evaluation % hilarious)

