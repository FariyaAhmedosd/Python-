marks=float(input("Enter your marks: "))
if(marks>=80 and marks<=100):
  print("Congratulation!!! YOu got A+")
elif(marks>=70 and marks<=80):
  print("well done! YOu got A")
elif(marks>=60 and marks<=70):
  print("Good YOu got A-")
elif(marks>=50 and marks<=60):
  print("YOu got B")
elif(marks>=40 and marks<=50):
  print(" YOu got C")
elif(marks>=33 and marks<=40):
  print("Good YOu got D")
elif(marks>0 and marks<33):
  print("Sorry! You have Failed! Good luck for next time.")
else:
  print("You have entered invalid  number.Enter a valid number between 1-100 ")