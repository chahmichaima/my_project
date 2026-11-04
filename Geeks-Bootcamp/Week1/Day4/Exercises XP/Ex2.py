#A movie theater charges different ticket prices depending on a person’s age.
#if a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10.
#if they are over the age of 12, the ticket is $15.
#How much does each family member have to pay ?
#Print out the family’s total cost for the movies.
#Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
family ={
    "rick":13,
    "beth":13,
    "morty":5,
    "summer":8
}
totale_cost=0
print("---prix des billets pour chaque membre---")
for name,age in family.items():
    if age<3:
        price=0
    elif 3<= age <=12:
        price=10
    else:
        price=15
    totale_cost += price 
    print(f"{name.capitalize()} a {age} ans et doit payer : ${price}")
print("-"*48)
print(f"cout total pour la famille :${total_cost}")