from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script" % (user_name, script))
print("I'd like to ask you a few questions")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)


print("""
      Alright so you said %s about liking me.
      You live in %s, city of raptors.
      And you have a %s computer.
      """ % (likes, lives, computer))
