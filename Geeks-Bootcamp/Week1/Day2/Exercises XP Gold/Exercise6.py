#Ask the user to input a number from 1 to 9 (including).
#Get a random number between 1 and 9. Hint: random module.
#If the user guesses the correct number print a message that says “Winner”.
#If the user guesses the wrong number print a message that says “Better luck next time.”
#Bonus: use a loop that allows the user to keep guessing until they want to quit.
#Bonus 2: on exiting the loop, tally up and display total games won and lost.
import random
l=0
w=0
q=1
while  q != 0:
    n1=random.randint(1,9)
    n2=int(input("input a number from 1 to 9 :"))
    if n1==n2:
        print("winners.")
        w=w+1
    else:
        print("better luck next time.")
        l=l+1 
    q=int(input("you wanna repeat again (0/1)"))
    
print("total won :{} total lost:{}".format(w,l))

