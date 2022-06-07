import random
from art import amogus
#Welcoming words
print(amogus)
print("Welcome to the Guess the Number Game!\nIm thinking a number between 1 - 100.")
def play_game():
  #Generate random number in range 1 - 100
  ANSWER = random.randint(1, 100)
  #debugging
  CLUE = f"(The number is {ANSWER})"
  print(CLUE)
  #Difficulty choosing
  DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if DIFFICULTY == "easy":
    ATTEMPT = 10
  else:
    ATTEMPT = 5
  #Game function
  is_true = False
  while not is_true:
    remaining_attempt = f"You have {ATTEMPT} attempt left to guess the number"
    print(remaining_attempt)
    #Guessing mechanism
    guess = int(input("Make a guess: "))
    #If the guess is higher than the answer
    if guess > ANSWER:
      print("Too high.\nGuess again.\n")
      ATTEMPT -= 1
      if ATTEMPT == 0:
        return print("You've run out of guesses, you lost.")
    #If the guess is lower than the answer
    elif guess < ANSWER:
      print("Too low.\nGuess again.\n")
      ATTEMPT -= 1
      if ATTEMPT == 0:
        return print("You've run out of guesses, you lost.")
    #If its a right guess
    elif guess == ANSWER:
      return print(f"\nYou got the answer! It was {ANSWER}")




#Calling the game function

play_game()
end_of_game = False
while not end_of_game:
  play_again = input("\nType 'y' to play again, 'n' to stop: ")
  if play_again == "y":
    play_game()
  elif play_again == "n":
    end_of_game = True
  else:
    print("YES (y) or NO (n)??!!")

  