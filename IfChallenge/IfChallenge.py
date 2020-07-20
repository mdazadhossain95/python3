# write a small program to ask for a name an age
# when both values have been e-ntered, check if the person
# is the eight age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# if they are, welcome them to the holiday, othereise print
# 	a (polite) messege refusing them entry

name = input("please enter your name")
age = int(input("How old are you, {0}?".format(name)))
print((age))

if 18<=age<=31:
	print("welcome to club 18-30 holidays, {0}".format(name))
else:
	print("Sorry, you can't go for holidays."
		  " better luck next time")
