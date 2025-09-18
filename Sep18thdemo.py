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
