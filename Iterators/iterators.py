string = "1234567890"

for char in string:
	print(char)

print("=======================================")

# my_iterator = iter(string)
# print(my_iterator)cha
#
# my_iterator = (next(my_iterator))
# my_iterator = (next(my_iterator))
# my_iterator = (next(my_iterator))
# my_iterator = (next(my_iterator))
# my_iterator = (next(my_iterator))
# my_iterator = (next(my_iterator))
# my_iterator = (next(my_iterator))
# my_iterator = (next(my_iterator))
# my_iterator = (next(my_iterator))
#
# print(next(my_iterator))

print("=======================================")

for char in string:
	print(char)
print("=======================================")


for char in iter(string):
	print(char)