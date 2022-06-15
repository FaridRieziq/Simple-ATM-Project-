
class Bank:
	def __init__(self):
		self.balance=0
		print("Halo!!! Selamat datang di Mesin ATM")

	def deposit(self):
		amount=float(input("Masukkan jumlah yang ingin ditabung : "))
		self.balance += amount
		print("\n Uang yang Anda tabung :",amount)

	def withdraw(self):
		amount = float(input("Masukkan jumlah yang Anda ingin tarik : "))
		if amount <= 50000:
			print("Maaf penarikan harus diatas 50 ribu")
		elif self.balance>=amount:
			self.balance-=amount
			print("\n Uang yang Anda tarik:", amount)
		else:
			print("\n Maaf saldo Anda kurang, saldo anda saat ini : ", self.balance)

	def cekSaldo(self):
		print("\n Saldo Anda saat ini =",self.balance)