#Keep asking the user to input the longest sentence,
#  they can without the character “A”.
#Each time a user successfully sets a new longest sentence,
#  print a congratulations message.
count=0
sen=""
while count==0:
    sen =input (" input the longest sentence they can without the character “A”:")
    if  "A" in sen:
            print("try again please.")     
    else:
            count=1
            print("congratulations.")
            break
