# Method	Description
# clear()	Removes all the elements from the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()
print("clear")
print(car)
print("=" * 30)

# copy()	Returns a copy of the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()
print("copy")
print(x)
print("=" * 30)

# fromkeys()	Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print("fromkeys")
print(thisdict)
print("=" * 30)

# get()	Returns the value of the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print("get")
print(x)
print("=" * 30)

# items()	Returns a list containing a tuple for each key value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()
print("item")
print(x)
print("=" * 30)

# keys()	Returns a list containing the dictionary's keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print("keys")
print(x)
print("=" * 30)

# pop()	Removes the element with the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")
print("pop")
print(car)
print("=" * 30)

# popitem()	Removes the last inserted key-value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()
print("popitem")
print(car)
print("=" * 30)

# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")
print("setdefault")
print(x)
print("=" * 30)

# update()	Updates the dictionary with the specified key-value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})
print("update")
print(car)
print("=" * 30)

# values()	Returns a list of all the values in the dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
print("values")
print(x)
print("=" * 30)
