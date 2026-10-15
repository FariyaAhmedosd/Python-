#defining function
def avg():
  a=int(input("Enter  number 1: "))
  b=int(input("Enter  number 2: "))
  c=int(input("Enter  number 3: "))
  average=(a+b+c)/3
  print(average)

#function call
avg()
avg()
avg()

def Goodbye():
   name = input("Enter your name: ")
   print(f"Goodbye,{name}")


Goodbye()
#built in function_already python e thake
#user defined function: user kokhono na kokhono define kore

#**functions with arguments
def goodDay(name,greet):
   print("Good day," +name)#string concatenation
   print(greet)

goodDay("Punom","Thank you")
goodDay("Tayeba","Thank you")
goodDay("Tanjina","Thank you")
#return value
def add_numbers(a,b):
   result=a+b
   return result
#function call and keep the return value in a variable
output = add_numbers(5,10)
print(output)
#user input in function call

def BTS():
   idol=input("Enter the name of the idol:")
   age=int(input("Enter the age: "))
   print(f"name of the member is {idol} & his age is :{age}")

BTS()# function e parameter nile user input neya jay na
BTS()
BTS()
BTS()
BTS()
BTS()
BTS()
#default parameter
