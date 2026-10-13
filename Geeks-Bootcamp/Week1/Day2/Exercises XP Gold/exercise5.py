#Ask the user for 3 numbers and print the greatest number
liste=[]
for i in range(3):
    n=int(input("give me  nmbre:" ))
    liste.append(n)
    n=0

print(max(liste))