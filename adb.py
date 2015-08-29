#!/usr/bin/python3

# A program that manage your contacts and the addresses
# Author: Flaymond Darius 

# NOTE: You must create a file named data.db first

import fileinput		# used in replace_contact	

adbFile = 'data.db'		# the database file, to save the contacts


# This will append the contact name & address to the data.db file
def add_contact():												
	name = input("Please enter the contact name: ")					# Prompt for the contact informations
	ads = input("Please enter the email address of the contact: ")
	
	data = "Name: {0}    Address: {1} ".format(name, ads)			# Just making it more clearly to read from data.db
	
	
	with open(adbFile, 'a') as f:				# open data.db as f, then write/append the data with newline
		f.write(data+"\n")

# This will find the text and replace the text
	
def replace_contact():
	sctext = input("Text to search for?: ")				# Text to search to replace
	screplace = input("Replacing with?: ")				# Replacing the searched letters with?
	
	for line in fileinput.input(adbFile, inplace=True):			# for everyline in data.db, replace the letter that match
		print(line.replace(sctext, screplace), end='')


# Simply find if contact available in data.db
def find_contact():
       
       
        f = open(adbFile)									# prompt
        choice = input("Who to find?(type 0 to quit): ")
        
        
        while True:										# while True, readline, and if the contact name/address found in the file,
            line = f.readline()							# print (yourchoice) is available
            if choice in line:
                print(choice + " is available")
                break
                
            elif choice  == '0':						# else if choice is equal to 0, break and exit the program
                print("Bye!")
                exit(0)
                
            else:										
               print(choice + " is not found in our database.")		# else, print (yourchoice) is not found in the database
               break

        find_contact()								# Loop the function/method again.
        


# Simply replace the text's with blank space(s)	
def delete_contact():							
	while True:
		sctext = input("Who to erase? (type 0 to quit): ")		# prompt -> which letter to delete
		
		for line in fileinput.input(adbFile, inplace=True):			# for matched line with words in the file, replace the matched letters with blank space
			print(line.replace(sctext, ""), end='')
			
		if '0' in sctext:								# if user type 0, program will exit immediately (after Bye! printed)						
			print("Bye!")
			exit(0)
			
def main():																# Prompts
	print("\n")
	print("Available options")
	print("\n1.Add new contact\n2.Find available contacts")
	print("3.Replace contact\n4.Delete available contact")
	choice = input("Please choose your option in integer(type 0 to quit): ")
	
	if choice == '1':											# Go through depends on the user choice
		add_contact()
	elif choice == '2':
		find_contact()
	elif choice == '3':
		replace_contact()
	elif choice == '4':
		delete_contact()
	else:
		print("Error occured")
		exit(0)
		
if __name__ == '__main__':
	main()
