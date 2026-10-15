import random
choices=[1,2,3,4,5,6]
dice=random.choice(choices)#random.randint(1,6)use kore loop chalate parbo
roll=int(input("Roll the dice (from 1 to 6): "))
print(f"computer choose: {dice}")
print(f"You choose: {roll}")
if(dice==roll):
  print("You both choose same")
else:
  if(dice<roll):
    print("You win!")
  elif(dice>roll):
    print("you lose!")



