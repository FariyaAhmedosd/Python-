

import random
def game():
  print("You are playing the game..")
  score = random.randint(1, 100)
  print(f"your current score is {score}")
  return score


def update_highScore():
  current_score = game()
  try:
    with open("hiscore.txt", "r") as f:
      content = f.read()
      if content == "":
        hiscore = 0
      else:
        hiscore = int(content)
  except FileNotFoundError:
    hiscore = 0

  print(f"Previous High score: {hiscore}")

  if current_score > hiscore:
    print(f"🎉 Awesome! You broke the high score: {current_score}")
    with open("hiscore.txt", "w") as f:
      f.write(str(current_score))
  else:
    print("Could not break the high score. Try again!")


update_highScore()

 
  