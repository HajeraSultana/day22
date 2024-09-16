print("+++Totally Random Number+++")
print()
print("Guess the number between 1 and 1,000,000 and I will tell you if you are too low, too high or get it correct.")
print()
print("Let's play!")
print()
import random
correct_number = random.randint(1,1000000)
attempt = 1
while True:
  myNumber = random.randint(1,1000000)
  user_guess = int(input("Pick a number between 1 and 1,000.000:"))
  if user_guess < 0:
    print("Now we'll never know what the answer is ...")
    exit()
  if user_guess < correct_number:
    print("That number is too low. Try again!")
    attempt += 1
    print()
  elif user_guess > correct_number:
    print("That number is too high. Try again!")
    attempt += 1
    print()
    continue
  elif user_guess == correct_number:
    print ("It took you", attempt, "shots to hit the mark!")
    break
  else:
    print("That is not a number I recognize.")