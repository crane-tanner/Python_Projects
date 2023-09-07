import random
# Include an ASCII art logo.
print(""" 
   _____                         _  _      _____                      
  / ____|                      _| || |_   / ____|                     
 | |  __ _   _  ___  ___ ___  |_  __  _| | |  __  __ _ _ __ ___   ___ 
 | | |_ | | | |/ _ \/ __/ __|  _| || |_  | | |_ |/ _` | '_ ` _ \ / _ \
 | |__| | |_| |  __/\__ \__ \ |_  __  _| | |__| | (_| | | | | | |  __/
  \_____|\__,_|\___||___/___/   |_||_|    \_____|\__,_|_| |_| |_|\___| \n\n""")

def play_game():
    def check_guess():
      if guess > number:
        print( "Too high") 
      elif number > guess:
        print("Too low")
      else:
        print(f"Correct, the number is {guess}. You win!")
        
    def set_difficulty():
        difficulty = input("Please choose a difficulty. Type 'easy' or 'hard'. \n")
        if difficulty == 'easy':
           return 10
        else: 
           return 5
    
    
    wrong_guess = True
    number = random.randint(1,100)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = set_difficulty()
    
    while wrong_guess:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check_guess()
        if guess == number:
          wrong_guess = False
        else: 
          attempts -= 1
        if attempts == 0:
          print("Game over. You ran out of attempts.")
          wrong_guess = False
    again = input("Would you like to play again? Type yes or no. \n")
    if again == 'yes':
        play_game()
        

play_game()

    