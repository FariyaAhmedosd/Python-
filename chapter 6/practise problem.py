num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
num4=int(input("Enter number 4: "))
if(num1>num2 and num1>num3 and num1 >num4):
  print("Number 1 is maximum")
elif(num2>num1 and num2>num3 and num2>num4):
  print("Number 2 is maximum")
elif(num3>num1 and num3>num2 and num3>num4):
  print("Number 3 is maximum")
elif(num4>num1 and num4>num2 and num4>num3):
  print("Number 4 is maximum")
#problem 2
marks1=int(input("Enter marks of AI: "))
marks2=int(input("Enter marks of ML: "))
marks3=int(input("Enter marks of DS: "))
total_percentage =(100*(marks1+marks2+marks3))/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
  print("Yoy are passed. Your total percentage is ",total_percentage)
else:
  print(" sorry!You failed!Try again next year. Your total percentage is ",total_percentage)
