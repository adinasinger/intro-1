# file with percentage grade for each student in class
#open file with percentage grades
#read file
#parse name and grade

# convert % grade to letter grade
#for each % grade, compare to range for letter grade (if statements)
#return letter grade

#append or write letter grade back to file

# download file as .txt

def convert_score_to_letter(score):
    #write conditionals that convert score number to letter
    #returns a letter based on each conditional
    	if score >= 90:
    		letter_Grade = "A"
    		return letter_Grade
    	elif score >= 80:
    		letter_Grade = "B"
    		return letter_Grade
    	elif score >= 70:
    		letter_Grade = "C"
    		return letter_Grade
    	elif score >= 60:
    		letter_Grade = "D"
    		return letter_Grade
    	else: 
    		letter_Grade = "F"
    		return letter_Grade


def process_file_to_list():
    #open the file
    #read the file into a list
    #return the list
    with open(class_grades.txt) as my_file: 
    	my_file.readline()

def main():
    #call function to process file and save the list to variable
    #iterate through the list and convert the score to letter
    #print the score and the letter it converts to
    #list1 = [80, 25, 100]
    for i in list1:
    	print convert_score_to_letter(i)
    
if __name__ == '__main__':
   main()