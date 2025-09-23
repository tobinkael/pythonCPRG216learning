#primitive data types

x = 2 #int
y = 3.2 #float
z = "Herro" #string

condition = True #boolean

# values of an expression

input("Enter your name: ") #does this have a value (output)
#yes, user provides value

age = 2025 - 1990 #35 will be the variable

#boolean expressions

# We are trying to answer a question.
# the answer is either yes or no (True or False)
# Our answer to this question is the value of the expression

#Example

3>4 #is this a boolean expression?
#yes, it will be false. 3 is not bigger than 4
# The value of this expression will be false, boolean.

var = 3 > 4 # logical xpression
# what is the type of var
print(var,type(var))  # boolean


# choosing the variable name
# by convention people use a question for the variable name of
# a boolean expression

is_adult = age >= 18 

# provide 3 variable names for boolean variable

atleast18 = age >= 18
meets_age_requirements = age >= 18





is_even = (age %2 == 0) # equality check operator
print("Age is even?", is_even) #false
# logical operators > < >= <= ==

is_absent = True
is_sick = True
is_child = False #convention

# list the logical operators

# Larger than >
# Larger than or equal >=
# Smaller than <
# Smaller than or equal <=
# equal ==
# not equal to !=

print ( "is 3>4?", 3 > 4)
print ( "is 3<=4?",3 <= 4)
print ( "is 3 equal to 5?", 3 == 5)
print ( "is 5 greater than or equal to 5?", 5>=5)
print ("is age greater than 35?",age>35)
print ("is 4 and 5 not equal?", 4!=5)


# IF STATEMENTS <<<<<<<<<<<<

# "if (keyword, is a must)"
# boolean/logical (is a must)
# : is a must
# indentation (must have)
# one or more statements of any type

#example
# " : " this means "then" in an if statment
if 3>4:
    print("yarp")
    print("3 is greater than 4")
    #Form of if statement, indentation keeps it part of the IF statement
    #since this statement is false it will not run, it only runs if true
#You can make the above statement true by reversing the greater/less than expression

# What is a statement? A complete instruction

if 4<5:
    print("4 is bigger than 5")

#testing/example/trying on own
print("Hello, I will check if your number is positive or negative")
numb = int(input("Enter a whole number"))

if numb < 0:
    print("She's negative")
else:
    print ("She's positive")


#Teacher example

age = int(input("What is your age?"))

is_adult = age >= 18

if is_adult:
    print("You can buy alcohol")
else:
    print("Sorry, you cannot buy alcohol")


# ::::::if else form:::::::
# "if (keyword, is a must)"
# boolean/logical (is a must)
# : is a must
# indentation (must have)
# one or more statements of any type
# non indented else (optional)
# ":" colon (is a must after else)
# needs indentation
# one or more statements ( Is a must if you use else)


