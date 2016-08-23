
# Code Workshop - Dictionary Shopping list.
#This program will do the following.
# 0 - Main Menu
# 1 - Show all lists.
# 2 - Show a specific list. 
# 3 - Add a new shopping list.
# 4 - Add an item to a shopping list.
# 5 - Remove an item from a shopping list.
# 6 - Remove a list by nickname.
# 7 - Exit when you are done.
# '''

# LET'S WRITE SOME SKELETON CODE!
shop_dict= {"Target": ["socks", "soap", "detergent", "sponges"], "Safeway": ["butter", "cake", "cookies", "bread"]}

def menu_prompt():
    # todo: display menu and get choice using raw_input from user.
    prompt = int(raw_input("0 - Main Menu\n1 - Show all lists.\n2 - Show a specific list. \n3 - Add a new shopping list.\n4 - Add an item to a shopping list.\n5 - Remove an item from a shopping list.\n6 - Remove a list by nickname.\n7 - Add multiple items to a list.\n8 - Write lists to file\n9 - Exit when you are done.\n"))
    return prompt


def show_all_lists():
    # todo: display all key:value pairs in dictionary
    return shop_dict.items()



def show_sorted_list(key):
    # todo: check if key is in dictionary, then print sorted list value
    if key in shop_dict: 
        print sorted(shop_dict[key])
    else:
        print "There is no list for that store.  Check your spelling or select option 3 to add a new one!"
    

def add_new_list(key):
    # add a new list with key as name of the list
    # make sure a list with this name doesn't already exist
    # deal with uppercase/lowercase
    if key not in shop_dict:
    	shop_dict[key]= []
    else:
    	print "It's already on the list."

def parse_items(string):
    parsed_string_list = string.split(",")
    for item in parsed_string_list:
        item.strip(" ")

    return parsed_string_list    


def add_item_to_list(key, item):
    # add an item to an existing list
   
    # check to see key exists
    # if item exists, let user know
    # then add item to list

    if key not in shop_dict:
    	print "You haven't created a list for this store. Choose option 3 on main menu."
    elif item in shop_dict[key]:
    	print "You already have this item on your list for %s." % (key)
    else:
    	shop_dict[key] = shop_dict[key] + [item]
	return (shop_dict[key])
    
    # deal with uppercase/lowercase
    


def remove_item_from_list(key, item):
    # todo:
    pass


def remove_list(key):
    # todo:
    pass

def write_to_file(file_name, key):
    with open(file_name, mode="w") as my_file:
        for item in shop_dict[key]:
            my_file.write(item)
            my_file.write("\n")


def main():
    # this is where the core logic will be
    # start by calling the menu prompt to return the user's choice
    prompt = menu_prompt()
    if prompt == 1:
        print show_all_lists()

 #if option 2 entered   
    if prompt == 2:
        key_name = raw_input("Which store list do you want? ")
        show_sorted_list(key_name)
        
 # if option 3 entered
    elif prompt == 3:
        new_key = raw_input("What store do you want to add a shopping list for? ")
        add_new_list(new_key)
        
 # if option 4 entered
    elif prompt == 4:
        key_name4 = raw_input("What store list do you want to add your item to? ")
        add_item = raw_input("What item do you want to add? ")
        add_item_to_list(key_name4,add_item)
        show_sorted_list (key_name4)

# if option 8 entered
    elif prompt == 8:
        write_to_file("test_write_file.txt","Target")

# testing adding multiple parsed items   
    # else:
    #     add_mult_items = raw_input("Which items do you want to add? (Use a comma to separate) ")
    #     print parse_items(add_mult_items)


if __name__ == "__main__":
    main()