#Ask the user to input a month (1 to 12).
#Display the season of the month received:
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)
n=int(input("input a month:"))

while n<1 or n>12:
   n=int(input("please input a number (1 to 12)"))

winter=[12,1,2]
spring=[3,4,5]
summer=[6,7,8]
autumn=[9,10,11]

if n in winter:
    print("it is winter")
elif n in spring :
    print("it is sprint ")
elif n in summer :
    print("it is summer ")
else:
    print("it is autumn")



