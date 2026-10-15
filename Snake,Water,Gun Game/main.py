'''
1 for snake
-1 for water
0 for gun
import random
computer = random.choice([-1,0,1])
youstr=input("Enter your  choice:")
youDict ={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"Gun"}#dictionary key:value
you=youDict[youstr]
#dictionary te user jeta enter korse sheta dibo r erpor value younum e assign kore dao
#water enter korle -1,gun =0,snake=1 assign korbe
print(f"Computer choose {reverseDict[computer]}\n You choose {reverseDict[you]}")

'''
import random
choices=["snake","water","gun"]
computer=random.choice(choices)
you=input("Enter  your choice: ")
print(f"computer choose: {computer}")
print(f"you choose: {you}")
if(computer==you):
  print("it's a Draw!!")
else:
  if(computer=="snake" and you=="gun"):
    print("You win!")
  elif you == "snake" and computer == "gun":
    print("You Lose!")
  elif you == "water" and computer == "gun":
    print("You Win!")
  elif you == "water" and computer == "snake":
    print("You Lose!")
  elif you == "gun" and computer == "snake":
    print("You Win!")
  elif you == "gun" and computer == "water":
    print("You Lose!")
  else:
    print("Invalid input! Please enter snake, water, or gun.")
 

  
    