class Phone:
	def __init__(self):
		print("I am in Phone class")

class Iphone(Phone):
	#init
	def __init__(self):
		super(Iphone, self).__init__()
		print("I am in Iphone class")

I = Iphone()