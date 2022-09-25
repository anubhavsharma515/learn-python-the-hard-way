from sys import exit


def gold_room(options):
    print("This room is full of gold. How much do you take?")
    show_options(options)

    next = int(input("> "))
    selected_option = options.get(next)

    print("You have decided to %s" % selected_option)
    if not(selected_option is None):
        how_much = next
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Nice, you're not greedy. You win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room(options):
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door")
    print("How are ytou going to move the bear?")
    print("Options are:")

    bear_moved = False
    
    show_options(options)
    
    while True:
        next = int(input("> "))
        selected_option = options.get(next)

        print("You have decided to %s" % selected_option)

        if selected_option == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif selected_option == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through the door now.")
            bear_moved = True
        elif selected_option == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off")
        elif selected_option == "open door" and bear_moved:
            gold_room(gold_room_user_options)
        else:
            print("I got no idea what that means")
    
def cthulhu_room(options):
    print("Here you see the evil Cthulhu")
    print("He, it, whatever stares at you and you go insane")
    print("Do you flee for your life or eat your own head?")
    show_options(options)

    next = int(input("> "))
    selected_option = options.get(next)

    print("You have decided to %s" % selected_option)

    if selected_option == "flee":
        start()
    elif selected_option == "head":
        dead("Well that was tasty!")
    else:
        cthulhu_room(options)

def set_options(options_list):
    options = {}
    number_of_options = len(options_list)

    for num in range(0, number_of_options):
        options[num] = options_list[num]

    return options

def show_options(options):
    for option_number, option_name in zip(options.keys(), options.values()):
        print(option_number, ":", option_name)

def dead(why):
    print(why, "Good job -.-")
    exit(0)

def start():
    print("you are in a dark room")
    print("There is a door to your left and right")
    print("Which one do you take?")

    next = input("> ")
    if next == "left":
        bear_room(bear_room_user_options) 
    elif next == "right":
        cthulhu_room(cthulhu_room_user_options)
    else:
        dead("You stumble around the room until you starve")

bear_room_user_options =  set_options(["take honey", "taunt bear", "open door"])
cthulhu_room_user_options =  set_options(["flee", "head"])
gold_room_user_options = set_options(["0", "1"])

start()

