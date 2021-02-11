# program that asks user for number and prompts user to guess number untill the user guess the right number 
# helen o'shea
# 20210211

import random

number = random.randint(0,100)
guess = int(input("Please guess the number between 0 and 100: "))
attempt = 1
while guess!=number:
  if guess<number:
    attempt +=1
    guess = int(input("your guess is too low please guess again: "))
    
  else:
    attempt += 1
    guess = int(input("your guess is too high please guess again: ")) 
print("you guessed {} correctly in {} attempts".format(guess, attempt))        