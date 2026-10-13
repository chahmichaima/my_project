#Ask the user for a number and a length.
#Create a program that prints a list of multiples of the number until
#the list length reaches length.


nmbr=int(input("input a number :"))
leng=int(input("input a length:"))
listy=[]
i=1
for i in range(1,leng+1):
    re=nmbr*i
    listy.append(re)
print(listy)