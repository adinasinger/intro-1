import library
from string import ascii_lowercase
#from library import add_numbers, subtract_num
def main():
	input1=int(raw_input("Enter a number: "))
	input2=int(raw_input("Enter another number: "))
	print library.add_numbers(input1,input2)
	print library.subtract_num(input1,input2)
	print ascii_lowercase

if __name__ == '__main__':
	main()