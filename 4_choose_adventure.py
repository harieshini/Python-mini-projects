name =input("Enter your name: ")
print("Welcome", name, "to this adventure game!")

answer=input("You are at the end of this dirt road . Would you like to proceed over to left or right?")

if answer.lower()=="left":
    answer=input("You have come to a river, you can walk around it or swim across (walk/swim) : ")
    
    if answer.lower()=="swim":
        print("You swam across and were eaten by an alligator!")
    
    elif answer.lower()=="walk":
        print("You walked for many miles , ran out of water and lost the game!")

    else:
        print("Not a valid option. You lose. ")

elif answer.lower()=="right":
    answer=input("You came to the dangling bridge! Do you want to cross it or return?(cross/return)  ")
    
    if answer.lower()=="cross": 
        print("You entered the lost city of Marsmallows!.Explore further!(yes/no)")

        if answer=="yes":
            print("You Got 200 marshmallows as a Gift ! Congratulations!")
        elif answer=="no":
            print("Awww! See you next time! ")
        else:
            print("Not a valid option. You lose. ")
        
    elif answer.lower()=="return":
        print("You got attacked by the alligator ! You lose!")

    else:
        print("Not a valid option. You lose. ")

else:
    print("Not a valid option. You lose. ")

print("Thank you for exploring The Adventure Game! ",name)