import random
secret_number = random.randint(1,10)
guess_count=0
guess_limit=3
out_of_guesses = False
print("Welcome to Number Guessing Game!")
print("Computer has already taken a number from 1 to 10")
while guess_count<=guess_limit and not out_of_guesses:
  guess=int(input("Enter your guessing number: "))
  guess_count+=1
  if(guess==secret_number):
   print("Congrats!!You guessed right")
   break
  else:
    print("Take another guess")
  if(guess_count==guess_limit and guess!=secret_number):
   print(f"sorry! you have no more chance! The right number was:{secret_number}") 