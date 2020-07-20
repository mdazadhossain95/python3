name = input("please enter your name")
age = int(input("How old are you, {0}?".format(name)))
print((age))

if age>=18:
	print("You are old enough to vote")
	print("please put an X in the box")
else:
	print("please come back in {0} years".format(18 - age))
print("==========================================================")

print("please guess a number between 1 and 10 : ")
guess = int(input())

if guess !=5:
	if guess < 5:
		print("please guess higher")
	else:
		print("please guess lower")

	guess = int(input())
	if guess == 5:
		print("well done, you guessed it")
	else:
		print("sorry, you have not guessed correctly")
else:
	print("you got it first time")
