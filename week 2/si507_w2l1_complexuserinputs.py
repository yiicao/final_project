# -*- coding: utf-8 -*-
"""SI507_W2L1_ComplexUserInputs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WWQz8tV69of_yU2zHMEaUnfBCCc5N5CY

# **Welcome to SI 507 Week 2 Lesson 1: Complex Uses of User Input.**

# (https://tinyurl.com/y6egzg64)

### **Review Basics of User Input**
![picture](https://drive.google.com/uc?export=view&id=1TAWCfqxLaXIiMzPJaob5qIlt0jMY9K_5)

As discussed previously, and as practiced in the Week 1 homework, the built-in function `input()` accepts user input in the form of a string by default.

The built-infunctions of `int()` and `float()` can convert a string into an integer or float. 

Nesting the `input()` function within an `int()` or `float()` function can require the user input to be an integer or 

Let's play with these examples.

**Best Practice: before executing the code, pause the video and make a prediction about what you think will happen. Doing this will engage metacognition and let you make deeper insights**
"""

name = input("What's your name?")

name = input("What's your name? ")
print("Hello, "+ name + "!")

age = input("How old are you? ")

age+4  #if you entered '35' before for age, what do you think this command will output?

age = int(age)    #what is this command doing?
age+4          #now what do you expect the output of this command to be?

age = int(input("How old are you? ")) # what if a child is answer 8.5
age+4          #now what do you expect the output of this command to be?

age = input("How old are you? ") # what if a child is answer 8.5
age=float(age)   #what is this command doing?
age+4          #now what do you expect the output of this command to be?

"""Reflection question: Order `str`, `int` and `float` from most restrictive to least restrictive.

Reflection question: why not use `float()` instead of `int()` all the time?

If you need more practice on what a string is, and how you can manipulate it, work through the exercises here: https://www.w3schools.com/python/python_strings.asp

##**Validation**
Validation can be used to further constrain the user input so that it's useful later. Built-in string functions can be used in validation

*   `isalnum()`	Returns `True` if all characters in the string are alphanumeric
*   `isalpha()`	Returns `True` if all characters in the string are in the alphabet
*   `isdecimal()`	Returns `True` if all characters in the string are decimals
*   `isdigit()`	Returns `True` if all characters in the string are digits
*   `isidentifier()`	Returns `True` if the string `is an identifier
*   `islower()`	Returns `True` if all characters in the string are lower case
*   `isnumeric()`	Returns `True` if all characters in the string are numeric
*   `isprintable()`	Returns `True` if all characters in the string are printable
*   `isspace()`	Returns `True` if all characters in the string are whitespaces
*   `istitle()`	Returns `True` if the string follows the rules of a title
*   `isupper()`	Returns `True` if all characters in the string are upper case

Lets look at an example of how to use `isalpha()` in combination with conditionals to ensure that user input is only alphabetical.
"""

#before running this code pause the video 
#use comments to annote the lines of the code
#is the output what you expect? 
name = input("what is your name? ")
if not name.isalpha():
  print("That's not a name I can use. Sorry.")
else:
  print("Hello ", name, "!")

"""Reflection: How can we get rid of the space between the name and the exclamation point in the printed output?

Lets examine a more complicated example. 

```
print("Gas Tank Refeuling light")
print("/\" * 10)  #what does this line do?

GasLevel = input("What percent full is the gas tank?")

if GasLevel > 50:
  print("We have enough gas")

elif GasLevel > 10:
  print("We need to get more gas soon")

else: 
  print("Please stop at the very next gas station!")
```

Do you know what should be printed if the user enters 55? or 45? or 10?

This code will not run as written. Can you figure out why? Pause the video and take a few minutes to think it through. Use comments to annotate the code. 

Hint: Should the user enter % or not?

If you still can't figure it out try running it below.
"""

print("Gas Tank Refeuling light")
print("/\\" * 10)  #what does this line do? #did it do what you predict

GasLevel = input("What percent full is the gas tank? ")

if GasLevel > 50:
  print("We have enough gas")

elif GasLevel > 10:
  print("We need to get more gas soon")

else: 
  print("Please stop at the very next gas station!")

"""We could use a nested `int(input())` command as previously disrupted but that would create an error and stop the program. What if we want to prompt the user to give a proper input? 

we can do that with a `while` loop using the `while True...break` pattern.
"""

print("Gas Tank Refeuling light")
print("/\\" * 10)  #what does this line do? #did it do what you predict
while True:
  GasLevel = input("What percent full is the gas tank? (exclude the % sign)")
  if GasLevel.isnumeric():
    GasLevelInteger= int(GasLevel)
    break  #why is this necessary?

if GasLevelInteger > 50:
  print("We have enough gas")

elif GasLevelInteger > 10:
  print("We need to get more gas soon")

else: 
  print("Please stop at the very next gas station!")