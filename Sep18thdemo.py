#This is our third class demo.
"""
this is a multi line
comment
in this demo we will work on variables,
operators and such
"""

# Review
# Assignment

a = 3
b = 3.5
c = True
d = "whats crackin"

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

# Some call functions

# print
# type
# input
# casting - if manual: EXPLICIT casting
# promoting/demoting - the more precise or the
# larger amount of memory allocated is "higher"

num_as_text = "43" #this cannot be used as a variable

num_as_num = int(num_as_text) #converting string(text) to num
print(num_as_text,type(num_as_text))
print(num_as_num,type(num_as_num))

num = 3
num_f = float(3)
num2 = 3.4
num2_i = int(num2)
num2_as_text = str(num2)



#using input function....Note input function always return a string

yob = input("Please Enter Your Rear of Birth\n")
print("your age is",int(2025)-int(yob))


#Calculate the area of any square


width = input("Enter the width:")
length = input("Enter The Length:")


result = int(width) * int(length)
print(result)


#print function
    #working with a separator
print("Hello", "Twitter World")
 # this will print Hello Twitter World
print("Hello", "Twitter World", sep=",")
 # this will print Hello, Twitter World
print("Hello", "Twitter World", sep=",", end=".")
 # this will print Hello, Twitter World.
print("Hello,\ttwitter world") 
 # this will print Hello,   twitter world
print("Hello, \nTwitter World")
 # this will print Hello,
 #                 Twitter World
 #If you want to print a "\" without triggering the escape characters use 
 #  \\
 # (\") to print [,] (\') to print [']



#Precedence Rules<<<<<<<<<<<<<<<<<<<<<<<<<

expression = 3+4*0-300+12/3

print(expression)

expression2 = 4/2*3

print(expression2)

# in expressions, follow bedmas unless equal ranks, then left to right

# More about assignments

x = 3
x = x + 5
print(x)

#increases X by 5

#can we shorthand this expression

x += 5 # this is equivalent to x = x + 5
#other examples of this same idea
print(x)
x -= 3 # x-2
print(x)
x *= 4 # x*2
print(x)
x **= 4 #x**2
print(x)



