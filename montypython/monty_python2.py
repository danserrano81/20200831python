#!/usr/bin/python3
round = 0
answer = " "

while round < 3:
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    
    # transform answer into something "common" to test
    answer = answer.lower()
    
    # Correct answer
    if answer == "brian": # logic to check if user gave correct answer
        print("Correct!")
        break # you gave an answer...escape the while loop!
	
    # easter egg
    elif answer == "shrubbery":
        print("You gave the secret answer!")
        break # you gave an answer...escape the while loop!
    # if counter reaches 3
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")
