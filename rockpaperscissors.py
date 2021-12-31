import random
possible_choices = ["rock", "paper", "scissors"]
#-----------------------------------------------------------------------------------------------------------------#
#ASKING THE USER IF THEY WANT TO PLAY THE GAME
print("Hello World")
print("This is my Rock Paper Scissors game.")
want_to_play = input("Would you like to play?")
want_to_play = want_to_play.lower()

if want_to_play == "yes": 
  print("Beginning Game.\nEnjoy.")
  runUserCode = True
elif want_to_play.lower() == "no":
  print("Ouch.")
  runUserCode = False
else:
  print("Invalid Entry.")
  runUserCode = False

userPoints = 0
computerPoints = 0 

#-----------------------------------------------------------------------------------------------------------------#
while runUserCode:
  print("\n")
  #ASKING USER FOR THEIR CHOICE
  user_choice = input("Choose one: Rock, Paper, or Scissors.")
  user_choice = user_choice.lower()

  #RANDOMIZES COMPUTER'S CHOICE
  computer_choice = random.choice(possible_choices)
  print(f"The computer chose {computer_choice}.")
  computer_choice = computer_choice.lower()

  #COMPARES CHOICES AND DETERMINES THE WINNER AND POINT ALLOCATION
  if user_choice == computer_choice:
    print(f"It's a tie! Both players chose {user_choice}")
    print("No points were awarded")

  elif user_choice == "rock":
    if computer_choice == "scissors":
      print("Rock beats Scissors! You win!")
      userPoints = userPoints + 1 
    elif computer_choice == "paper":
      print("Paper beats Rock. You lose.")
      computerPoints = computerPoints + 1
    else:
      print("")

  elif user_choice == "paper":
    if computer_choice == "rock":
      print("Paper beats Rock! You win!")
      userPoints = userPoints + 1
    elif computer_choice == "scissors":
      print("Scissors beats Paper. You lose.")
      computerPoints = computerPoints + 1
    else:
      print("")

  elif user_choice == "scissors":
    if computer_choice == "paper":
      print("Scissors beats Paper! You win!")
      userPoints = userPoints + 1
    elif computer_choice == "rock":
      print("Rock beats Scissors. You lose.")
      computerPoints = computerPoints + 1
    else:
      print("")

  #ASKS THE USER IF THEY'S LIKE TO PLAY AGAIN
  print("\n")
  play_again = input("Would you like to play again?")
  print("\n")
  play_again = play_again.lower()
  
  #CONTINUES THE GAME AFTER DISPLAYING THE SCORE AND WHO IS WINNING
  if play_again == "yes":
    print(f"You have {userPoints}.")
    print(f"The computer has {computerPoints}.")

    if userPoints == computerPoints:
      print(f"You are tied at {userPoints}")
    elif userPoints > computerPoints:
      user_lead = userPoints - computerPoints
      print(f"You are winning by {user_lead}")
    elif userPoints < computerPoints:
      computer_lead = computerPoints - userPoints
      print(f"The computer is winning by {computer_lead}")
    else:
      print("")
    print("\n")
    continue
  #ENDS THE CODE AFTER DISPLAYING THE FINAL SCORE
  elif play_again == "no":
    print("\n")
    print("FINAL SCORE")
    print(f"You ended with {userPoints}.")
    print(f"The computer ended with {computerPoints}.")
    print("Thank you for playing!")
    runUserCode = False

  #ASKS THE USER TO ANSWER THE QUESTION AGAIN WITH A CORRECT ANSWER
  else:
    print("Invlaid Entry.\nPlease answer with Yes or No.")
    play_again = input("Would you like to play again?")
    print("\n")
    play_again = play_again.lower()
    
    if play_again == "yes":
      print(f"You have {userPoints}.")
      print(f"The computer has {computerPoints}.")

      if userPoints == computerPoints:
        print(f"You are tied at {userPoints}")
      elif userPoints > computerPoints:
        user_lead = userPoints - computerPoints
        print(f"You are winning by {user_lead}")
      elif userPoints < computerPoints:
        computer_lead = computerPoints - userPoints
        print(f"The computer is winning by {computer_lead}")
      else:
        print("")
      print("\n")
      continue
    elif play_again == "no":
      print("\n")
      print("FINAL SCORE")
      print(f"You ended with {userPoints}.")
      print(f"The computer ended with {computerPoints}.")
      print("Thank you for playing!")
      runUserCode = False
  
