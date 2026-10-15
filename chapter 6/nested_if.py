num=int(input("Enter a number: "))
if(num>=1):
   print("It is a positive number")
   if(num%2):
     print(" & It is a even number")
   else:
     print(" & It is a odd number")
elif(num==0):
  print("Number is non negative")
else:
  print("it is a negative number")