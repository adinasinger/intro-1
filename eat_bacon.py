#should you eat that bacon flowchart

def coward():
	warrior = raw_input("Are you a coward?")
	if warrior.upper() == "NO":
		print "Then eat it."
	elif warrior.upper() == "YES":
		print "Bacon will turn you into a true warrior."

def main():
	tastebuds = raw_input("Do you wantto feel like angels are frolicking on your taste buds? ")
	if tastebuds.upper() == "YES":
		print "Eat it!"
	if tastebuds.upper() == "NO":
		print "You've clearly never tasted bacon. Eat it!"
	if tastebuds.upper() == "MAYBE":
		coward()


		
if __name__ == '__main__':
	main()
