import random
print(' Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + " Rock vs Paper -> Paper wins \n"
      + " Rock vs Scissors -> Rock wins \n"
      + " Paper vs Scissors -> Scissor wins \n")

def get_user_choice():
    while True:
        user_choice = input(" Enter your choice:\n Rock \n Paper \n Scissors \n")
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print(" Invalid choice. Please choose rock, paper or scissors. ")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def declare_winner(user_choice,computer_choice):
      if user_choice==computer_choice:
        return " It's a Tie! "
      elif (user_choice == 'rock' and computer_choice == 'scissors') or\
            (user_choice == 'scissors' and computer_choice == 'paper') or\
            (user_choice == 'paper' and computer_choice == 'rock'):
            return " You Win! "
      else:
         return " Computer Wins! "
    
user_score = 0
computer_score = 0

while True:
     user_choice = get_user_choice()
     computer_choice = get_computer_choice()

     print(f" You chose {user_choice}. Computer chose {computer_choice}. ")

     result = declare_winner(user_choice, computer_choice)
     print(result)

     if result == " You Win! ":
          user_choice += 1
     elif result == " Computer Wins! ":
          computer_score += 1

     print(f" Score -\n User: {user_score}\n Computer: {computer_score}")
     
     start_again = input(" Do you want to play again? (yes/no): \n\n").lower()
     if start_again != 'yes':
         break
print(" Thanks for playing!😀😀 ") 