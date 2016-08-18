food_price_tuple = ('sushi', 7.50, 'burrito', 8.20, 'cheeseburger', 6.00, 'hot dog', 3.40, 'fried rice', 9.99)

def convert_tuple_to_dictionary(input_tuple):
	food_dictionary = {}
	for item in input_tuple:
		if isinstance(item,str):
			food_dictionary[item] = 0
	print food_dictionary.items()

convert_tuple_to_dictionary(food_price_tuple)

