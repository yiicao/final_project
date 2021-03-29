# -*- coding: utf-8 -*-
"""SI507_W2L2_BasicFunctions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XYJx_mttQ0v1VHJ5M6NF7jNCn7oCz9uR

# **Welcome to SI 507 Week 2 Lesson 2: Basic Functions.**

# https://tinyurl.com/y6mblg8s 

Why do programmers use functions?

![picture](https://drive.google.com/uc?export=view&id=1ZpjDQOJy1sB3gjD2DqoadVN8ghWREfwn)

Functions make your programs more **readable**, by hiding **complexity**. The **reusability** of functions lets you efficiently complete, repeated tasks. 

Functions fulfill the programming edict of 'Dont Repeat Yourself' (DRY).

**DRY** code is preferable to **WET** (Write Every Time) code. 

Using functions prevents typo errors.

Let's look at some examples to illustrate this concept.



**Best Practice: before executing the code, pause the video and make a prediction about what you think will happen. Doing this will engage metacognition and let you make deeper insights**
"""

## Before hitting run make a prediction about the output!
SalesPeople = {
    '1001': {'last_name': 'C', 'first_name': 'Alan', 'uniqname': 'AlanC'},
    '1002': {'last_name': 'R', 'first_name': 'Keisha', 'uniqname': 'RKeisha'},
    '1003': {'last_name': 'W', 'first_name': 'Tanya', 'uniqname': 'WTanya'},
    '1004': {'last_name': 'D', 'first_name': 'Henry', 'uniqname': 'DHenry'}
}
sales = {
    '1001': [190, 188, 175, 195],   
    '1002': [192, 199, 288, 140],
    '1003': [195, 188, 182, 110],
    '1004': [99, 292, 94, 298]
}

'''
many lines in between
'''  

max = 0
max_id = -1
for id in sales:
    sum = 0
    num_sales = 0
    for s in sales[id]:
        sum = sum + s
        num_sales += 1
    avg = sum/num_sales
    if avg > max:
        max = avg
        max_id = id
print(SalesPeople[max_id])

"""You can figure out the above code with some careful attention. But its not hard to imagine that if it was many lines longer you wouldn't be able to tell what it is.

Now imagine instead there was just the following two lines:
```
top_salesperson = find_salesperson_with_highest_weekly_sales_average(SalesPeople, sales)
print(top_salesperson)
```

that's much more interpretable, but does it run?

Only if this accompanies it:
```
def find_salesperson_with_highest_weekly_sales_average(SalesPeople, sales):
  max = 0
  max_id = -1
  for id in sales:
    sum = 0
    num_sales = 0
    for s in sales[id]:
        sum = sum + s
        num_sales += 1
    avg = sum/num_sales
    if avg > max:
        max = avg
        max_id = id
  return SalesPeople[max_id]

```
The complexity isn't erased - its just hidden.

When you use multiple functions in a short space, the readability becomes much much better than compared to WET code. 

```
top_salesperson = find_salesperson_with_highest_weekly_sales_average(SalesPeople, sales)
send_email(top_salesperson['uniqname'] + '@widgets4sale.com', "Great Job!")
```

##Reusability
Run the code in the following cell. Make a prediction and look at the output
"""

SalesPeople = {
    '1001': {'last_name': 'C', 'first_name': 'Alan', 'uniqname': 'AlanC'},
    '1002': {'last_name': 'R', 'first_name': 'Keisha', 'uniqname': 'RKeisha'},
    '1003': {'last_name': 'W', 'first_name': 'Tanya', 'uniqname': 'WTanya'},
    '1004': {'last_name': 'D', 'first_name': 'Henry', 'uniqname': 'DHenry'}
}
sales = {
    '1001': [190, 188, 175, 195],   
    '1002': [192, 199, 288, 140],
    '1003': [195, 188, 182, 110],
    '1004': [99, 292, 94, 298]
}

def find_salesperson_with_highest_average(SalesPeople, sales):
    max = 0
    max_id = -1
    for id in sales:
        sum = 0
        num_sales = 0
        for s in sales[id]:
            sum += s
            num_sales += 1
        avg = sum/num_sales
        if avg > max:
            max = avg
            max_id = id
    return SalesPeople[max_id]

def compute_final_sales(sales):
    salesperson_sales = {}
    for id in sales:
        sum = 0
        num_sales = 0
        for s in sales[id]:
            sum += s
            num_sales += 1
        salesperson_sales[id] = sum/num_sales
    return salesperson_sales

def print_final_sales(SalesPeople, final_sales):
    for id in final_sales:
        salesperson = SalesPeople[id]
        print(salesperson['first_name'], salesperson['last_name'], 'has', final_sales[id])

top_salesperson = find_salesperson_with_highest_average(SalesPeople, sales)
print("The top salesperson is", top_salesperson['first_name'], top_salesperson['last_name'])

final_sales = compute_final_sales(sales)
print_final_sales(SalesPeople, final_sales)

"""Now look at the code, you will see that it’s a completed version of the program we’ve been looking at so far, with two new functions `compute_final_sales()`  and `print_final_sales()`. Look at these and try to figure out what they do.


This program can be simplified. There is some repeated code in it. Identify the repeated code and convert it into a function to make the program simpler. This may take a substantial amount of time pause the video and work on it. If you are stuck. Explain where you're stuck and post a comment in the slack in the lecture channel. Myself or one of your peers will respond.
"""

### Refactored Code

SalesPeople = {
    '1001': {'last_name': 'C', 'first_name': 'Alan', 'uniqname': 'AlanC},
    '1002': {'last_name': 'R', 'first_name': 'Keisha', 'uniqname': 'RKeisha'},
    '1003': {'last_name': 'W', 'first_name': 'Tanya', 'uniqname': 'WTanya'},
    '1004': {'last_name': 'D', 'first_name': 'Henry', 'uniqname': 'DHenry'}
}
sales = {
    '1001': [190, 188, 175, 195],   
    '1002': [192, 199, 288, 140],
    '1003': [195, 188, 182, 110],
    '1004': [99, 292, 94, 298]
}

def compute_average(num_list):
    sum = 0
    num_items = 0
    for n in num_list:
        sum += n
        num_items += 1
    return sum/num_items

def find_salesperson_with_highest_average(SalesPeople, sales):
    max = 0
    max_id = -1
    for id in sales:
        avg = compute_average(sales[id])
        if avg > max:
            max = avg
            max_id = id
    return SalesPeople[max_id]

def compute_final_sales(sales):
    salesperson_sales = {}
    for id in sales:
        salesperson_sales[id] = compute_average(sales[id])
    return salesperson_sales

def print_final_sales(SalesPeople, final_sales):
    for id in final_sales:
        salesperson = SalesPeople[id]
        print(salesperson['first_name'], salesperson['last_name'], 'has', final_sales[id])

top_salesperson = find_salesperson_with_highest_average(SalesPeople, sales)
print("The top salesperson is", top_salesperson['first_name'], top_salesperson['last_name'])

final_sales = compute_final_sales(sales)
print_final_sales(SalesPeople, final_sales)

"""**Refactoring** is *rewriting a program so that the structure of the code changes but the functionality does not.*

### **Review Basics of Functions**
![picture](https://drive.google.com/uc?export=view&id=1pfA5WOqR-wFUCqXCFNI4zsoFdnJq_XQs)

**The syntax of a function**

```
def function_name(argument1, argument2):
  '''docstring 
     docstring '''
  indented statement
  indented statement
  return value
```
*  `def` is: keyword
*  `function_name` is: function name 
*  `argument1` & `argument2` are the arguments and they are *positional*
*  `       `indentation defines the body of the function that is executed whenever the function is called
*  `'''docstring'''` is an explanation of what the function does. It has a specified syntax which we will discuss in depth!
*  `value` is the data that the `return` keyword sends back to the program when a function is called.

**Scope**

All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.
The **scope** of a variable determines the portion of the program where you can access a particular identifier. 

There are two basic scopes of variables in Python:
*  Global variables
*  Local variables

*Global vs. Local variables*
Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.
This means that local variables can be accessed only inside the function in which they are declared whereas global variables can be accessed throughout the program body by all functions. When you call a function, the variables declared inside it are brought into scope.

Test your understanding by working through the following examples.
"""

var1 = 66 # global scope
def func1():
    print("inside function", var1) # global name is valid inside the function
func1()
print("outside function", var1) # global name is valid outside the function

### Test your knowledge: Global vs Local
var2 = 77 # global scope
def func2():
    var2 = 88 # local name overrides global
    
    print("inside function", var2) 
func2()  # What do you think will print here, 88 or 77?
print("outside function", var2) # What do you think will print here, 88 or 77?

#Test your knowledge Global vs Local
def func3():
    var3 = 99 # local name overrides global
    print("inside function", var3) 
func3() #what do you think prints here?
print("outside function", var3) #what do you think prints here?

def func4(param1):
    print("inside function A", param1) 
    param1 = 222
    print("inside function B", param1) 
var4  = 111
func4(var4)  ### two print statements are called here. What values will print?
print("outside function", var4) # What value is going to print here?

####
#### func5 is constructed differently than func4.
#### 
def func5(var5):
    print("inside function A", var5) 
    var5 = 222
    print("inside function B", var5) #### what will function B print?  isnt var5 a global variable?
var5  = 111
func5(var5)  
print("outside function", var5)  ### what will this line print? isn't var 5 a global variable?

def func6(var6):
    var6 += " world"
    print(var6, "from func6") 
var6  = "hello"
func6(var6)   #what do you expect to print here? 
print(var6, "from indent level 0")   #What do you expect to print here?

"""# **Mutability**

Most data types in python are mutable.

Numbers, booleans, strings and tuples are immutable
"""

### This example works intuitively
string1 = "I am a string"
print(string1[3])
tuple1 = (1, 2, 3)
print(tuple1[2])
List1 = ['hat', 4, 3.2626]
print(List1[-1])

####
#### Two of the not work....Why not?
####
string1 = "I am a string"
#string1[3] = "n"
print(string1[3])

tuple1 = (1, 2, 3)
#tuple1[2] = 4
print(tuple1[2])

List1 = ['hat', 4, 3.2626]
List1[-1] = 'temecula'
print(List1[-1])

"""Lists are mutable, tuples and strings which are handled verys similarly - are not.

String.functions therefore return *new* strings.
"""

s1 = "hello"
s2 = s1.upper()
print(s1, s2)

"""The mutability of variables has important consequences for what happens to arguments during functions. Let's look at some simple examples."""

x = 5
y = x 
print(x) # prints ?
print(y) # prints ?

x = 6
print(x) # prints 6
print(y) # does this print 5 or 6?

"""Now lets do it with strings"""

s = "hello"
s2 = s 
print(s) # prints "hello"
print(s2) # prints "hello"
s = "world"
print(s) # prints "world"
print(s2) # prints hello or world?

"""Even mutable types will have this predictable behavior -- if you don't 'mutate' them."""

a = [1, 2, 3]
b = a
print(a) # prints "[1, 2, 3]"
print(b) # prints "[1, 2, 3]"
a = [4, 5, 6]
print(a) # prints "[4, 5, 6]"
print(b) # prints ?

"""But things can get mutated!"""

#### this example is not intuitive -- pay attention.
a = [1, 2, 3]
b = a
print(a) # prints "[1, 2, 3]"
print(b) # prints "[1, 2, 3]"
a.append(4)
print(a) # what will print?
print(b) # what will print?
b.append(5)
print(a) # prints "[1, 2, 3, 4, 5]"
print(b) # prints "[1, 2, 3, 4, 5]"
a = [4, 5, 6]
print(a) # prints "[4, 5, 6]"
print(b) # prints "[1, 2, 3, 4, 5]"

"""So lets finally look at this phenomenon in the context of functions."""

def change_it(the_list):
    the_list.append('d')

g_list = ['a', 'b', 'c']
change_it(g_list)
print(g_list) # prints "['a', 'b', 'c', 'd']"

def dict_update(local_dict):
    local_dict['g'] = 'grapefruit'
    local_dict['n'] = 'nectarine'
global_dict = {'g': 'grape', 'p': 'plum', 'o': 'orange'}
dict_update(global_dict)
print(global_dict['g']) #what will print?
print(global_dict['n']) #what will print?
print(global_dict['p'])

"""This happens because `the_list` and `local_dict` are pointers to their global counterparts - not full copies!"""

def list_remind(message, data):
    print('2', message, data[-1])
    message = 'don\'t forget!'
    data.append('eggs')
    print('3', message, data[-1])

groceries = ['milk', 'bread']
reminder = 'please pick up'
print('1', reminder, groceries[-1])
list_remind(reminder, groceries)
print('4', reminder, groceries[-1])