import random

user_wins=0
comp_wins=0
moves=["rock","paper","scissors"]
print("Welcome to Rock-Paper-Scissors!")

while True:
    user_input=input("Your Move or q to Quit: ").lower()
    if user_input=="q":
        break

    if user_input not in moves:
        continue
    
    random_num=random.randint(0,2)
    
    comp_pick=moves[random_num]
    print("Computer picked",comp_pick + ".")
    
    if user_input=="rock" and comp_pick=="scissors":
       print("You Win! ")
       user_wins+=1
    
    elif  user_input=="paper" and comp_pick=="rock":
       print("You Win! ")
       user_wins+=1
    
    elif user_input=="scissors" and comp_pick=="paper":
       print("You Win! ")
       user_wins+=1
    
    elif user_input==comp_pick:
        print("It's a draw! ")
    
    else: 
        print("You Lose! ")
        comp_wins+=1

print("You won", user_wins,"times")
print("Computer won ",comp_wins,"times")      