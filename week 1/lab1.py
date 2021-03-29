# -*- coding: utf-8 -*-
"""Lab 1

1. Getting Started:

Please install python on your desktop. If you took SI 506 with Professor Whyte you already did this. In case you are working on a new machine or did not take his course installation instructions are below for Mac, PC & Ubuntu. Visual Studio Code is our recommended environment -- but it is not required. 


Python Installation
*   Windows 10: https://github.com/umsi-arwhyte/SI506-2020Winter/blob/master/docs/install/win-install-pysf_python.md
*   Mac: https://github.com/umsi-arwhyte/SI506-2020Winter/blob/master/docs/install/mac-install-pysf_python.md
*   Ubuntu: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu



Visual Studio Code Installation
*   Windows 10: https://github.com/umsi-arwhyte/SI506-2020Winter/blob/master/docs/install/win-install_vscode_with_py_extension.md
*   Mac: https://github.com/umsi-arwhyte/SI506-2020Winter/blob/master/docs/install/mac-install_vscode_with_py_extension.md
*   Ubuntu: https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-20-04/

** please note we have not troubleshooted the ubuntu instructions.

2. To anchor your interest in learning python please write a short paragraph (at least 4 sentences) describing how you might use python in your discipline. Preferably focus on a use case involving databases, web APIs or one of the other methods taught in this course.  You can use your GSI's description of their projects from last year as inspiration.  (Remember to add # to make your response a comment so that this file remains runnable).
I don't like it at all but it looks like everyone should learn."""



# Working with User Inputs & Lists - Example Code
## Please work through the following code
## use in code comments to annotate anything you didn't remember from 506

zoo = ["monkey", "tiger", "eagle"]	# define a list
zoo[0]	# a single element
zoo[0] = "gorilla"	# change an element
zoo.append("parrot")	# add elements at end of list
zoo = ["zebra","lion"] + zoo	# add elements at beginning
      
# creating and modifying a list
zoo = ["monkey", "tiger", "eagle", "parrot"]
print("The zoo has the following", len(zoo), "animals:", zoo)
print("The 1. animal is", zoo[0])
print("The 2. animal is", zoo[1])
print("The 1. and 2. animals are", zoo[:2])
print("Animals 2. - 4. are", zoo[1:4])
print("The animals after the 2. one are", zoo[2:])
print("The last element is", zoo[-1])
new_animal = input("Which animal would you like to add? ")
zoo.append(new_animal)
print("The zoo has the following", len(zoo), "animals:", zoo)
new_animal = input("Which animal should replace the monkey? ")
zoo[0] = new_animal
print("The zoo has the following", len(zoo), "animals:", zoo)

which_animal = int(input("Which number animal in the list should we print? "))
print("The number", str(which_animal), "animal in the list is ", zoo[which_animal - 1])

"""3. Using the example above please do the following

3A. Create a list that contains the names of 5 of your labmates. (you don't have to ask for input - just define the list yourself)

3B. Write a command to Print your list.

3C. Write a command that uses user-input to ask for an additional labmates name. Write a command to Append that name to the list

3D. Write a command to Print the appended list. 

3E.  Write a command that uses user-input to ask for a Number, and print the name in your list that has that number as index. (Frame the user-input question in a way that constrains the answers as necessary).

3F.  What is the error that you get if you use are provided a user input of 12?

3G. Bonus: Write a command using 'modulo' to eliminate the error in 3F regardless of the number the user inputs.
"""
labmates = ['a', 'b', 'c', 'd', 'e']
print(labmates) 
new_labmate = input("What extra labmate would you like to add?")
labmates.append(new_labmate)

## Example Code 2
del zoo[0]	# delete an element by index number
zoo.remove("tiger")	# delete an element by value
zoo.insert(1, "elephant")	# insert an element
len(zoo)	# length of zoo
max(zoo)	# alphabetically first or smallest element
min(zoo)	# alphabetically last or largest element
new_zoo = zoo[:]	# create a new copy of zoo
zoo.reverse()	# change the list to reverse order
zoo.sort()	# change the list to alphabetical order

# Deleting elements from a list
zoo = ["monkey", "tiger", "eagle", "parrot"]
print("The zoo has the following", len(zoo), "animals:", zoo)
number = int(input("Which animal would you like to delete? \
Input the number of the animal: "))
if 0 <= number < len(zoo):
  del zoo[number]
else:
  print("That number is out of range!")
print("The zoo has the following", len(zoo), "animals:", zoo)
new_animal = input("Which animal would you like to delete? \
Input the name of the animal: ")


if new_animal in zoo:
  zoo.remove(new_animal)
  print(new_animal, "has been deleted")
else:
  print(new_animal, "cannot be deleted because it is not in the zoo")
  print("The zoo has the following", len(zoo), "animals:", zoo)

"""4. Contintuing from your script from the prior exercise (in which you made a list of labmates names) please do the following:

4A. Write a command to Print the list.

4B. Write a command that asks the user to input the name, and checks whether that names is in the list. 

4C. Write a command that asks for user input of a name, and deletes that name if present in the list, and appends it if not. 

4D. Write a command that creates a copy of the list in reverse order.


4E. Print both the original list and the reverse list.
"""

# for statement
#
zoo = ["tiger", "elephant", "monkey"]
for animal in zoo:
  print(animal)

"""5. Using the list of student names from the previous question please do the following:

5A. Create a for loop that prints for each student "hello student_name, how are you?" where student_name is the name of each student in the list.

5B. Create a loop that asks the user whether to keep or delete each name. Delete the names which are no longer wanted. Hint: you cannot go through a list using a for loop and delete elements from the same list simultaneously because in that way the for loop will not reach all elements. You can either use a second copy of the list for the loop condition or you can use a second empty list to which you append the elements that the user does not want to delete.
"""

# Program to read and print a file
'''
file = open("Hail.txt","r")	## open for reading
file = open("output.txt","w")	## open for writing
file = open("output.txt","a")	## open for appending
file.close()	# close file
text = file.readlines() #	read all lines into a list called "text"
line = file.readline() #	read next line into a string called "line"
file.writelines(text)	# write list to file
file.write(line)	# write one line to file
'''
file = open("Hail.txt","r")
text = file.readlines()
file.close()
for line in text:
  print(line)

"""6. Write code (using a modified version of the above example code) that prints the lines of Hail.txt in reverse order.

7A. Write code that sends reverse-order Hail output to a new file named 'Reverse-Hail.txt' instead of on the screen. Make the commands overwrite Reverse-Hail.txt everytime it is run.

7B. Write code that sends the reverse-order Hail output to a new file named Reverse-Hail.txt, but make your commands append the output to that file each time it is run.

8. Extension: Write code that prints the lines of Hail.txt in reverse order - but also prints the line number at the beginning of each line.
"""
file = open("Hail.txt", "r")
text_reverse = reverse(file.readlines())
line = file.readline()
file.close()
file1 = open('Reverse-Hail.txt','w')
file1.writelines(text_reverse)
# remember what a dictionary is

relatives = {"Lisa" : "daughter", "Bart" : "son", "Marge" : "mother", "Homer" : "father", "Santa" : "dog"}
for member in relatives.keys():
  print(member, "is a", relatives[member])

"""10. Create a second dictionary called 'Age' with the same keys as relatives. Write a loop that prints the keys and elements of 'Age' in a meaningful sentence (as above).

11. Extension: write user input commands that ask the user for Abe Simpson's family member status and age and adds that information to the dictionary (e.g. grandfather/64). Use the 'string.isalpha()' and 'string.isnumeric()' commands to ensure that the user input only accepts alphabetical characters for the relatives dictionary and only numerical values for the Age dictionary. Use If and Else statemetns to reject Abe Simpson from each dictionary if the user input does not meeet the appropriate numerical/alphabetical standard.
"""