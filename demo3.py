e = 4%3
print(e, type(e)) # shows the remainder of the division, not the answer to the division

f = 3**2 # means power
print(f, type(f))

d_= 3//4 # floor division
print(d_, type(d_))

# combining variables ---->

e = f+d_ # process the assignment from right to left
# it means; evaluate a + b first, then add the results to the variable E


# I want to compute the circum and the area of the circle
# assume the circle radius is 5
# and that pi = 3.14

rdus = 5
pi = 3.14

circum = 2*pi*rdus 

print("The Circumference is:",circum,type(circum))

#static type vs dynamic type

x = 5 # it is a type (int)

x = 4.3 # x changes its type to (float)

x = "hello" # x changes its type to (string)

x = True # x changes to (bool)

print(x)

#this is a dynamic variable type in python because it will
#the type automatically.

g = 3 #int
h = 4 #int
z = g/h #float, automatic casting, so instead of Z being int
# it will be promoted to float

print(z,type(z))

#manual casting

int(z)
print(int(z))

#this rounds it to the smallest int, so for 0.75, it will go to 0

print(int("43"))

print(str(43))

x = 1
print(x, type(x))

y = float(x)
print(y,type(y)) #this is a promotion, promoted the int to float

v = 4.3
print(v, type(v))
u = int(v)
print(u,type(u)) #this is a demotion, we demoted V from float to int
#these are all examples of manual casting (explicit casting)


#circumference with user input>>>>>>>>>>>>>>
#ask the user to enter the circle radius

user_input = input("Enter the radius of the circle brotha: ")
pi = 3.14
rdus = int(user_input)
circum = 2*pi*rdus 

print("The Circumference is:",circum,type(circum))

