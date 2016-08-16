shopItems = ["eggs", "bread", "milk", "water"]
choice = 0

def menuChoice():
	global choice
	choice = int(raw_input("Enter 1 to add to list, 2 to remove from list, 3 to view current list, 4 to exit"))
	return choice

def addList(item):
	global shopItems
	if shopItems.count(item.lower()) != 0:
		print "You have already this item."
		menuChoice()
	else:
		shopItems.append(item)
		shopItems.sort()
		menuChoice()

	return shopItems

def removeList(item):
	global shopItems
	if shopItems.count(item.lower()) == 0:
		print "This item is not on the list."
	else:
		shopItems.remove(item.lower())
		shopItems.sort()
		menuChoice()

	return shopItems


def main():
	menuChoice()
	while (True):
		
		if choice == 4:
				break
		elif choice == 1:
			addedItem = raw_input("Enter your item to add: ")
			print addList(addedItem)
		elif choice == 2:
			removedItem = raw_input("Enter your item to remove: ")
			print removeList(removedItem)
		elif choice == 3:
			shopItems.sort()
			menuChoice()



if __name__ == '__main__':
	main()

