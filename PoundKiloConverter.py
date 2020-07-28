print("what you want to convert?")
print("1. kilogram to pound")
print("2. pound to kilogram")
number= input("if the first one then click 1 \n"
			  "or if the 2nd one then click 2 : ")
number1 = int(number)
if 0 < number1 < 2:
	print("how much kilogram want to convert?")
	kilogram = input("write hare : ")
	kilogram1 = float(kilogram)
	lbs = float(2.205)
	cal= kilogram1/lbs
	cal1 = float(cal)
	print(cal1)
	cal4 = str(cal1)
	kilogram = str(kilogram)
	print(kilogram + " kilogram = " + cal4 + " pound/lbs")
elif 1 < number1 < 3:
	print("how much pound/lbs want to convert?")
	pound = input("write hare : ")
	pound1 = float(pound)
	kg = float(0.45359237)
	cal3 = pound1 * kg
	cal2 = float(cal3)
	print(cal2)
	cal5 = str(cal2)
	pound = str(pound)
	print(pound + " pound/lbs = " + cal5 + " Kilogram")
else:
	print("your option is wrong,\nPlease rerun the program again.")




