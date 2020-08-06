menu = [
	["egg", "spam", "bacon"],
	["egg", "sausage", "bacon"],
	["egg", "spam"],
	["egg", "bacon", "spam"],
	["egg", "spam", "sausage", "bacon"],
	["egg", "spam", "sausage", "bacon"],
	["egg", "spam", "bacon", "sausage", "spam"],
	["egg", "spam", "bacon", "sausage"],
	["chicken", "chips"]
]

meals = []
for meal in menu:
	if "spam" not in meal:
		meal.append(meal)
	else:
		meals.append("a meal was skipped")
print(meals)

meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)

fussy_meals = [meal for meal in menu if "spam" in meal or "eggs" in meal
			   if not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

fussy_meals = [meal for meal in menu if ("spam" in meal or "eggs" in meal) if
			   not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)
