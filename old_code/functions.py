# Python 3
def yes_or_no(question):
	waiting = True
	while waiting:
		answer = str(input(question + " (y/n)")).lower()
		if answer == 'y':
			waiting = False
			return True
		elif answer == 'n':
			waiting = False
			return False
		else:
			print("Please enter y or n")

# car = yes_or_no("Do you own a car?")
# print(car)

def ask_amount(question):
	waiting = True
	while waiting:
		try:
			answer = int(input(question))
		except:
			print("Please enter a number (no decimals)")
			continue
		else:
			return answer
			waiting = False

# rent = ask_amount("How much rent do you pay?")
# print(rent)
