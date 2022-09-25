def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses" % cheese_count)
    print("You have %d boxes of crackers" % boxes_of_crackers)
    print("Dude that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly")
cheese_and_crackers(20, 30)

print("OR, we can use variables from within a script")

amount_of_cheese = 20
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print("OR, we can add math into the arguments")
cheese_and_crackers(20+5,30-4)

print("OR, we can add math into the arguments with variables!!")
cheese_and_crackers(amount_of_cheese+5,amount_of_crackers-4)
