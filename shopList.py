shopItems = ["eggs", "bread", "milk", "water"]
choice = 0

def makeChoice():
	global choice
	choice = int(raw_input("Enter 1 to add to list, 2 to remove from list"))
	return choice

def addList(item):
	global shopItems
	if shopItems.count(item.lower()) != 0:
		print "You have already this item."
		makeChoice()
	else:
		shopItems.append(item)
		shopItems.sort()

	return shopItems

def removeList(item):
	global shopItems
	if shopItems.count(item.lower()) == 0:
		print "This item is not on the list."
	else:
		shopItems.remove(item.lower())
		shopItems.sort()
	return shopItems


def main():
	makeChoice()
	if choice == 1:
		addedItem = raw_input("Enter your item to add")
		print addList(addedItem)

	if choice == 2:
		removedItem = raw_input("Enter your item to remove")
		print removeList(removedItem)

if __name__ == '__main__':
	main()

