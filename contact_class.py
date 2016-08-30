# class Contact(object): 
# 	def __init__(self, first_name, last_name, mobile_number ="", work_number ="", email =""): 
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.mobile_number = mobile_number
# 		self.work_number = work_number
# 		self.email = email
	
# 	def text(self, message): 
# 		if self.mobile_number is "": 
# 			print "no mobile number exists" 
# 		else:  
# 			print "To: %s - %s" % (self.mobile_number,message)

from create_class import Contact

def main():
	contact_list =[]
	contact_name = raw_input("enter first name: ")
	contact_last_name = raw_input("enter last name: ")
	contact_mobile_number = raw_input("enter mobile: ")
	contact_work_number = raw_input("enter work number: ")
	contact_email = raw_input("enter email: ") 
	# contact2 = Contact("Adina", "Singer", "", "", "adinasemail@email.com")
	# contact3 = Contact("Brad", "Pitt")

	Contact(contact_name,contact_last_name,contact_mobile_number,contact_work_number,contact_email)
	# ADD TO CONTACT_LIST
	# contact_list.append(contact_name)
	# contact_list.append(contact_last_name)
	# contact_list.append(contact2)
	# contact_list.append(contact3)

	for contact in contact_list:
		print contact.first_name + " " + contact.last_name + " " + contact.mobile_number + " " + contact.work_number + " " + contact.email
		print contact.text("Here is your contact info in my address book")	

if __name__ == '__main__':
	main()