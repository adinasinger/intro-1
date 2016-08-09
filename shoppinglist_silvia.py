
list=["bread","cheese","milk","candy"] 


def shopping_list():
	choice=raw_input("what would you like to add to the shopping list?").lower()
	if choice in list: 
		print  "You already have it"
	else:
		list.append(choice)

	list.sort()
	print list


def remove_list_item():
	choice_remove=raw_input("Would you like to remove something from the shopping list?").lower()
	if choice_remove not in list:
		print "This item is not on the list"
	else:
		list.remove(choice_remove)

	list.sort()
	print list

def main():
	shopping_list()
	remove_list_item()


if __name__=='__main__': 
	main()
