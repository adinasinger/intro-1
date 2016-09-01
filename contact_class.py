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
from contact_ui import menu

def show_contacts():
	pass

def add_contact(contact_list_name):
	# ADD TO CONTACT_LIST
	# for each list item, check to see if first and last name combo already exists in list and give error message
	# check upper/lowercase
	print "contact list: ", contact_list_name
	name_to_add = raw_input("Enter first name of contact to be added: ")
	last_name_to_add = raw_input("Enter last name of contact to be added: ")
	contact_mobile_number = raw_input("enter mobile: ")
	contact_work_number = raw_input("enter work number: ")
	contact_email = raw_input("enter email: ") 
	
	if not contact_list_name:
		print "found empty list"
		contact1 = Contact(name_to_add,last_name_to_add,contact_mobile_number,contact_work_number,contact_email)
		contact_list_name.append(contact1)
		return contact_list_name

	for contact in contact_list_name:
		print "inside loop"
		print "contact: ", contact.first_name	
		if contact.first_name == name_to_add.lower() and contact.last_name == last_name_to_add.lower():
	 		print "This contact is already in the list"
	 		return	
		else:
			contact1 = Contact(name_to_add,last_name_to_add,contact_mobile_number,contact_work_number,contact_email)
			contact_list_name.append(contact1)
			return contact_list_name
	
	

def edit_contact():
	pass
def delete_contact():
	pass

def main():
	contact_list=[]
	
	contact2 = Contact("adina", "singer", "", "", "adinasemail@email.com")
	contact3 = Contact("Brad", "Pitt")
	# contact_list.append(contact_name)
	# contact_list.append(contact_last_name)
	contact_list.append(contact2)
	contact_list.append(contact3)

	choice = menu()
	print choice
	# contact_name = raw_input("enter first name: ")
	# contact_last_name = raw_input("enter last name: ")
	# contact_mobile_number = raw_input("enter mobile: ")
	# contact_work_number = raw_input("enter work number: ")
	# contact_email = raw_input("enter email: ") 
	
#option 2 - add a contact
	if choice == 2:
		add_contact(contact_list)
		
			
	

 	# print contact_list[0:5]
 	# print contact_list.items()
 	print [contact.first_name for contact in contact_list]

	# for contact in contact_list:
	# 	print contact.first_name + " " + contact.last_name + " " + contact.mobile_number + " " + contact.work_number + " " + contact.email
	# 	print contact.text("Here is your contact info in my address book")	
			

if __name__ == '__main__':
	main()