class phone:
	@staticmethod
	def call():
		print("You can call")

	@staticmethod
	def message():
		print("You can message")


class Iphone(phone):

	@staticmethod
	def photo():
		print("You can take photo")


Ip = Iphone
Ip.message()
Ip.call()
Ip.photo()
