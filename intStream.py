class intStream():
	currentValue = 0

	def eos(self):
		if self.currentValue+1 == 100000000:
			return True
		else:
			return False	

	def reset(self):
		self.currentValue = 0

	def next(self):
		if self.eos():
			print("EOS")
		else:
			self.currentValue+=1
			return self.currentValue

class primeStream(intStream):
	currentValue = 1

	def eos(self):
		if self.currentValue+1 == 18:
			return True
		else:
			return False

	def reset(self):
		self.currentValue == 1

	def	czyJestPierwsza(self, liczba):
		if liczba == 1:
			return True
		if liczba == 2:
			return True
		if liczba == 3:
			return True
			
		for i in range(2, liczba):
			if liczba % i == 0:
				return False
		return True			

	def next(self):
		if self.eos():
			print("koniec liczb pierwszych")
			self.reset()
			retrun -1
		liczba = self.currentValue+1
		czyLiczbaJestPierwsza = False
		while czyLiczbaJestPierwsza == False:
			if not self.czyJestPierwsza(liczba):
				liczba+=1
			else:
				czyLiczbaJestPierwsza=True
			if liczba == 18:
				print("koniec liczb pierwszych")
				self.reset()
				return -1
		self.currentValue = liczba
		return self.currentValue

p1 = primeStream()
print(p1.next())	
print(p1.next())			
print(p1.next())			
print(p1.next())
print(p1.next())
print(p1.next())