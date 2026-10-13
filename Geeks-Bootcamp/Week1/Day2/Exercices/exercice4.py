#Write code that will ask the user for their height in centimeters.
#If they are over 145cm print a message that states they are tall enough to ride.
#If they are not tall enough print a message that says they need to grow some more to ride.

H=float(input("Please enter your height in centimeters :"))
print("")
if H>145 :
    print("You are tall enough to ride .")
else:
    print("You are not tall enough  you need to grow a bit  more to ride")