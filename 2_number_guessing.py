import random 

max_range=int(input("Type a Number : "))
if max_range<=0:
    print("Please Enter a number larger than 0 next time!")
    quit()
r= random.randint(0, max_range)
guesses=0

while True:
    guesses+=1
    user_guess=int(input("Guess the number : "))
    if user_guess==r:
        print("You got it!")
        break
    elif  user_guess>r:
        print("You went higher than the number!")
    else:
        print("You went lower than the number!")
        
    
print("You Got it in ",guesses, "guesses")
