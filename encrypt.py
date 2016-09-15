def encrypt(message):
#encrypt message - how?
	crypto_dict = {"h":"1", "i":"*"}
	secret_msg = []
	for letter in message:
		code_num = crypto_dict[letter]
		secret_msg.append(code_num)
	print secret_msg	
#write encrypted msg to file
	with open("secret.txt", mode = "w") as my_file:
		my_file.write("not secret")

encrypt("hi")