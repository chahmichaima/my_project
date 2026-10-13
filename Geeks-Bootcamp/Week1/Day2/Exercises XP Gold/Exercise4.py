names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#Ask a user for their name, 
# if their name is in the names list print out the index of the first occurrence of the name.
#Example: if input is Cortana we should be printing the index 1

name=input("what is your name :")

if name in names :
    print(names.index(name))
else:
    print("name note found in the list.")