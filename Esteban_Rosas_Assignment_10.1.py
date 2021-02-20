# Author: Esteban
# Creation Date: 2/16/2021

# Use the OS module to validate the existance of a directory before creating a file there.
# Prompt the user to what directory they would like to save a file in and naming it.
# Prompt user for name, address, and phone number. 
# program will write this data to a comma separated line in a file.
# Program should then read file contents.

import os

check_directory = input('\nWhat is the directory you are looking for?: ')

def main():
   print ("\nDirectory exists: " + str(os.path.exists(check_directory)))

if __name__== "__main__":
   main()

if os.path.exists(check_directory):
    print ("\nIt looks like the directory already exists!")
    print("\n-------------------------------------------")
else:
    print ("\nIt does not look like the directory exists!")
    print("\n-------------------------------------------")
    new_path = input("\n Would you like to create this directory? (yes or no): ")
    if new_path == 'yes' or 'y':
        os.makedirs(check_directory)
        print("\nYour directory", check_directory, "is being saved!")
    else:
        print("\nNo directory was created.")



name_of_file = input("\nWhat is the name of the file you would like to save?: ")
completeName = check_directory + '/' + name_of_file + ".txt"

with open(completeName, 'w') as file_object:
    text_body1 = input("\nWhat is your name?: ")
    text_body2 = input("\nWhat is your address?: ")
    text_body3 = input("\nWhat is your phone number?: ")
    file_object.write(text_body1 + "\n")
    file_object.write(text_body2 + "\n")
    file_object.write(text_body3 + "\n")

with open(completeName) as file_object:
    contents = file_object.read()
    print("\n" + contents)