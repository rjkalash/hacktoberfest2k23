# I am going to write three lambda function which is also known as anonymous function
# in python lambda function can be written in below format
# name of the funtion or variable = lambda(keyword) input : operation or what you are going to __doc__
# the function can be called by the variablename(input)

a=lambda x: x*2
print(a(2))

# This is the lambda funciton which will double the input given

a=lambda x: True if x%2==0 else False
print(a(11))

#This is the lambda funciton to tell whether the input number is even or odd

a=lambda x,y,z: x+y+z
print(a(1,2,3))

#This is the lambda funciton to add three numbers
