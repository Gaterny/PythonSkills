import random

class GuessNumber(object):
	
	def __init__(self, max_num, min_num, chance):
		super(GuessNumber, self).__init__()
		self.max_num = max_num
		self.min_num = min_num
		self.chance = chance
		self.random_number = random.randint(min_num, max_num)

	def guess(self):

		chance = self.chance

		while chance > 0:
			chance -= 1
			try:
				num = int(input('please input your number:'))
			except ValueError as e:
				print('please input the correct number!')
				continue
			if num == self.random_number:
				print("Congratulations! lucky boy!")
			elif num <= self.random_number:
				print("your number is small, chance left %d" %chance)
			else:
				print("your number is big, chance left %d" %chance)
		else:
			print("It's a pity that you lose the game for %d times! The correct answer is %d" %(self.chance, self.random_number))

if __name__ == '__main__':
	game = GuessNumber(50,0,10)
	game.guess()
