print("price of the house is 1000000 million dollar or $1M")
number = input("if need to put down 10% then click 1 or \nif need to put down then click 2 : ")
number = int(number)
if 0 < number< 2 :
	total_parsentage = 1000000 * 0.1
	total_parsentage = float(total_parsentage)
	print(total_parsentage)
	total_parsentage = str(total_parsentage)
	print("Down Payment is " + total_parsentage + " dollar only")
elif 1 < number < 3:
	total_parsentage = 1000000 * 0.2
	total_parsentage = float(total_parsentage)
	print(total_parsentage)
	total_parsentage = str(total_parsentage)
	print("Down Payment is " + total_parsentage + " dollar only")
else:
	print("You type wrong,\nplease rerun the program again.")







