#Write a program that asks a string to the user,
# and display a new string with any duplicate consecutive letters 
# removed.
 
fir=input("input a string :")
new=""
for i in range(len(fir)):
    if i==0 or fir[i]!= fir[i-1]:
         new=new+fir[i]
print(new)