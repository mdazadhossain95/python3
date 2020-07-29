# cities = ["Dhaka", "Chittagong", "Kumilla", "Khulna", "Barishal"]
#
# with open("cities.txt", 'w') as city_file:
# 	for city in cities:
# 		print(city, file=city_file)
#----------------------------------------------
# cities = []
#
# with open("cities.txt", 'r') as city_file:
# 	for city in city_file:
# 		cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
# 	print(city)
#-----------------------------------------------

# imelda = "more mayhem", "Imedla MAy", "2011", (
# 	(1, "hello"), (2, "Hi"), (3, "azad"), (4, "Hossain")
# )
# with open("imelda3.txt",'w') as imelda_file:
# 	print(imelda, file=imelda_file)
#----------------------------------------------

with open("imelda3.txt", 'r') as imedla_file:
	contents = imedla_file.readline()
imedla = eval(contents)

print(imedla)
title, artist, year, track = imedla
print(title)
print(artist)
print(year)