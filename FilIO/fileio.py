jabber = open("C:/Users/mdaza/Desktop/1.txt")
# # jabber = open("1.txt","r")
#
# for line in jabber:
# 	print(line)
# 	# if "jabberwpck" in line.lower():
# 	# 	print(line, end='')
#
# jabber.close()

# with jabber as jabbers:
# 	for line in jabbers:
# 		if "MOD" in line.upper():
# 			print(line, end='')
# 			line = jabbers.readline()
#
# with jabber as jabbers:
# 	lines = jabbers.readlines()
# print(lines)
# for line in lines[::-1]:
# 	print(line, end='')

with jabber as jabbers:
	lines = jabbers.read()
for line in lines[::-1]:
	print(line, end='')