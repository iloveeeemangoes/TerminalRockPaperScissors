import random
import os

options = ["rock", "paper", "scissors"]


game = 1
score = 0
while game <= 3:
    terminal_width = os.get_terminal_size().columns

    print("-"*terminal_width)
    print("Game Number "+str(game))

    chosen_option = random.choice(options)
    guess = input("Rock,Paper,Scissors Shoot: ")
    print("Computer chooses "+ chosen_option)
    print("You choose " + guess)
    if chosen_option == "rock":
        if guess == "rock":
            print("Tie")
            score +=0
            game +=1
            print("Your Overall Score is "+str(score))

        elif guess == "paper":
            print("You win, paper beats rock")
            score +=1
            game +=1
            print("Your Overall Score is "+str(score))

        elif guess == "scissors":
            print("You lose, rock beats scissors")
            score +=0
            game +=1
            print("Your Overall Score is "+str(score))

        else:
            print("Unknown option, please input either rock, paper or scissors")
            score +=0
            game +=0
            print("Your Overall Score is "+str(score))

    elif chosen_option == "paper":
        if guess == "rock":
            print("You lose, paper beats rock")
            score +=0
            game +=1
            print("Your Overall Score is "+str(score))

        elif guess == "paper":
            print("Tie")
            score +=0
            game +=1
            print("Your Overall Score is "+str(score))

        elif guess == "scissors":
            print("You win, scissors beats paper")
            score +=1
            game +=1
            print("Your Overall Score is "+str(score))

        else:
            print("Unknown option, please input either rock, paper or scissors")
            score +=0
            game +=0
            print("Your Overall Score is "+str(score))

    else:
        if guess == "rock":
            print("You win, rock beats scissors")
            score +=1
            game +=1
            print("Your Overall Score is "+str(score))

        elif guess == "paper":
            print("You lose, scissor beats paper")
            score +=0
            game +=1
            print("Your Overall Score is "+str(score))

        elif guess == "scissors":
            print("Tie")
            score +=0
            game +=1
            print("Your Overall Score is "+str(score))

        else:
            print("Unknown option, please input either rock, paper or scissors")
            score +=0
            game +=0
            print("Your Overall Score is "+str(score)) 

print("")
print("* GAME OVER * " *10)
print("YOUR TOTAL SCORE IS " + str(score))