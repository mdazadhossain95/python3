import datetime
import pytz


class Account:
	"""Simple account class with balance"""

	@staticmethod
	def _current_time():
		utc_time = datetime.datetime.utcnow()
		return pytz.utc.localize(utc_time)

	def __init__(self, name, balance):
		self._name = name
		self.__balance = balance
		self.transaction_list = []
		self.transaction_list = [(Account._current_time(), balance)]
		print("Account created for " + self._name)

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			self.show_balance()
			self.transaction_list.append((Account._current_time(), amount))

	def withdraw(self, amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			self.transaction_list.append((Account._current_time(), amount))
		else:
			print("The amount must be greater than zero and no more then your account balance")
		self.show_balance()

	def show_balance(self):
		print("Balance is {}".format(self.__balance))

	def show_transactions(self):
		for date, amount in self.transaction_list:
			if amount > 0:
				tran_type = "deposited"
			else:
				tran_type = "withdraw"
			print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
	azad = Account("Azad", 0)
	azad.show_balance()

	azad.deposit(1000)
	azad.show_balance()
	azad.withdraw(500)
	# azad.show_balance()
	azad.withdraw(2000)

	azad.show_transactions()

	steph = Account("steph", 800)
	steph.__balance = 200
	steph.deposit(100)
	steph.withdraw(200)
	steph.show_transactions()
	steph._Account__balance = 40
	steph.show_balance()
	print(steph.__dict__)
