print("Welcome To the Quiz Game!")
play=input("Shall we Start?(yes/no)  ")

if play.lower()!="yes":
    quit()

print("Here We Go!")
score =0

answer=input("What does HTTP stand for? ")
if answer.lower() == "hyper text transfer protocol":
    print("That is correct! ")
    score+=1
else:
    print ("Oops that is not correct!")

answer=input("What does USB stand for? ")
if answer.lower() == "universal serial bus":
    print("That is correct! ")
    score+=1
else:
    print ("Oops that is not correct!")

answer=input("What does LAN stand for? ")
if answer.lower() == "local area network":
    print("That is correct! ")
    score+=1
else:
    print ("Oops that is not correct!")

answer=input("What does UDP stand for? ")
if answer.lower() == "user datagram protocol":
    print("That is correct! ")
    score+=1
else:
    print ("Oops that is not correct!")

answer=input("What does SSD stand for? ")
if answer.lower() =="solid state drive":
    print("That is correct! ")
    score+=1
else:
    print ("Oops that is not correct!")


print("You Got " + str(score) + " questions correct! Hurray!!")
print("Thank you for taking the quiz champ!")