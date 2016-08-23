menu_list = ["food:hotdog,price:5.50","food:burger,price:9.50",
       "food:fries,price:4.00","food:shake, price:5.00"]

def split_menu_items(menu_list):
#always define your dictionary first!
	item_prices = {}

	for item in menu_list:
		split_list = item.split(",")
		print split_list
#from split_list, should have two strings indexed in list to split again
		split_list_1 = split_list[0].split(":")
		print split_list_1


split_menu_items(menu_list)