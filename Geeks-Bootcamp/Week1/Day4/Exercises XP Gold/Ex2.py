birthdays = {
    "chaimaa": "1995/04/12",
    "salma": "1990/11/23",
    "salwa": "1998/07/05"
}

print("Noms disponibles dans le dictionnaire :")
for name in birthdays.keys():
    print(f"- {name}")
person_name = input("\nEntrez le nom d'une personne : ")
if person_name in birthdays:
    print(f"L'anniversaire de {person_name} est le {birthdays[person_name]}.")
else:
    print(f"Sorry, we don't have the birthday information for {person_name}.")