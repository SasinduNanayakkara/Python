import random

def randomNumber(): #random number generating function
  return random.randint(1,100)

def compare_number(guessNumber,user_number): #number comparing function

  if guess_number > user_number : 
    print("Too high\n Guess again")
    return False
  elif guess_number < user_number : 
    print("Too low \n Guss again")
    return False
  else:
    print(f"You got it! The answer was {user_number}")
    return True

def guess_difficulty(diffculty,guessNumber): #difficulty checking function
  if diffculty == "easy":
    attempts = 10
    
  elif diffculty == "hard":
    attempts = 5
    

  for i in range(attempts):

    print(f"You have {attempts - i} attempts remaining to guess the number.") 
    user_number = int(input("Make a guess : "))
    dicision = compare_number(guess_number,user_number)

    if dicision:
      break
    
  print("You've running out of guesses, You lose.")
    
  
import art
print(art.logo) #print the art

print("Welcome to the number guessing game!")
print("I'm guessing number between 1 to 100")
guess_number = randomNumber() #call the random number generator function

diffculty = input("Choose the difficulty. Type 'easy' or 'hard' :") 

guess_difficulty(diffculty,guess_number) #call difficulty checking function
