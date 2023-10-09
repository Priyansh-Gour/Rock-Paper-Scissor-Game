#Rock paper and scissors game

import random
user_won=0
computer_won=0

options=["rock","paper","scissors"]
while True:
    user_input=input("Choose rock ,paper or scissor or Q for quit ").lower()
    if user_input=="q":
        break
    if user_input not in options :
        print("Enter valid input ")
        continue
    random_number=random.randint(0,2)
    compurer_input=options[random_number]
    print("computer picked ",compurer_input)

    if user_input=="rock" and compurer_input=="scissors":
        print("You won ")
        user_won+=1
    elif user_input=="paper"and compurer_input=="rock":
        print("you won")
        user_won+=1
    elif user_input=="scissors"and compurer_input=="paper":
        print("you won")
        user_won+=1
    elif user_input==compurer_input:
        print("draw")
    else:
        print("computer won")
        computer_won+=1
print("you won ",user_won,"times")
print("computer won",computer_won,"times")
print("Good bye")
    
        

