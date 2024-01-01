import random

options = ["rock", "paper", "scissor"]

computer_point = 0
user_score = 0

exit = False
while exit == False:
    
    user_input = input("\nChoose rock, paper scissor or exit: ")
    computer_input = random.choice(options)
    
    if user_input == "exit":
        exit = True
    
    elif user_input == "rock":
        
        if computer_input == "rock":
            print("your input is rock ")
            print("computer input is rock")
            print("Tie \n")
        
        elif computer_input == "scissor":
            print("computer input is scissor")
            print("you win! \n")
            user_score += 1
        
        elif computer_input == "paper":
            print("computer input is paper")
            print("Computer wins ! \n" )
            computer_point += 1
    
    elif user_input == "paper":
        
        if computer_input == "paper":
            print("your input is paper ")
            print("computer input is paper ")
            print("Tie \n")
        
        elif computer_input == "scissor":
            print("computer input is scissor")
            print("you win! \n")
            user_score += 1
        
        elif computer_input == "rock":
            print("computer input is rock")
            print("Computer wins !\n ")
            computer_point += 1

    elif user_input == "scissor":
        
        if computer_input == "scissor":
            print("your input is scissor ")
            print("computer input is scissor")
            print("Tie \n")
        
        elif computer_input == "paper":
            print("computer input is paper")
            print("you win!\n")
            user_score += 1
        
        elif computer_input == "rock":
            print("computer input is rock")
            print("Computer wins !\n")
            computer_point += 1
    else:
        print("Error occurred\n ")

print(f"your score is {user_score} \ncomputer score is {computer_point}")
