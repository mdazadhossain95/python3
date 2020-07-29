# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
# 	print(animal)
#
# print("=" * 50)
#
# wild_animals = set(["lion", "tiger", "panther"])
# print(wild_animals)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)
#
#
# empty_set = set()
# empty_set_2 = {}
# empty_set.add("a")
# # empty_set_2.add("a")
#
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# square_tuple = (4, 6, 9, 16, 25)
# square = set(square_tuple)
# print(square)
# print(len(square))
#
# print(even.union(square))
# print(len(even.union(square)))
#
# print(square.union(even))
#
# print("-" * 50)
#
# print(even.intersection(square))
# print(even & square)
# print(square.intersection(even))
# print(square & even)

even = set(range(0, 40, 2))
print(even)
square_tuple = (4, 6, 16)
square = set(square_tuple)
print(square)
if square.issubset(even):
	print("square is a subset of even")

if even.issuperset(square):
	print("even is a superset of square")


#
# print("even minus square")
# print(sorted(even.difference(square)))
# print(sorted(even - square))
#
# print("square minus even")
# print(square.difference(even))
# print(square - even)
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(even)))
#
# print("symmetric square minus even")
# print(square.symmetric_difference(even))

# square.discard(4)
# square.remove(16)
# square.discard(8)
# print(square)
# if 8 in square:
# 	square.remove(8)
# except KeyError:
# 	print("The item 8 is mot a member of the set")

