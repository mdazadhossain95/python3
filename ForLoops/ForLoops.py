for i in range(1,20):
	print("i is now {}".format(i))
print("==================================")

number = "9,985,783,356,387,98756"
for i in range(0, len(number)):
	print(number[i])
print("==================================")

number = "9,985,783,356,387,98756"
CleanedNumber = ''

for i in range(0, len(number)):
	if number[i] in '0123456789' :
		CleanedNumber = CleanedNumber + number[i]
newNumber = int(CleanedNumber)
print("The number is {} ".format(newNumber))

print("==================================")

number = "9,985,783,356,387,98756"
CleanedNumber = ''

for char in number:
	if char in '0123456789' :
		CleanedNumber = CleanedNumber + char
newNumber = int(CleanedNumber)
print("The number is {} ".format(newNumber))

print("==================================")

for state in ["not pinin'", "no more", "a stuff", "bereft of life"]:
	print("This parrot is " + state)
	# print("This parrot is {}".format(state))

for i in range(0,100,5):
	print("i is {}".format(i))

for i in range(1, 13):
	for j in range(1, 13):
		print("{1} times {0} is {2}".format(j,i,i*j), end='\t')  # end='\t' it will make in one line in one time loops
	# print("=====================")
	print('|')
