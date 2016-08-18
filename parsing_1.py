def string_splitter():
	str1 = "item:apples,quantity:4,price:1.50\n"
	split_string = str1.split(",")

	qty_string = split_string[1].split(":")
	qty = int(qty_string[1])

	price_string = split_string[2].split(":")
	price = float(price_string[1])

	return price
print string_splitter()

