#Create a variable called birthdays. Its value should be a dictionary.
#Initialize this variable with the birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip: Use the format "YYYY/MM/DD".
#Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”
#Ask the user to give you a person's name and store the answer in a variable.
#Get the birthday of the name provided by the user.
#Print out the birthday with a nicely-formatted message


birthdays = {
    "chaimaa": "1995/04/12",
    "hiba": "1990/08.25", 
    "moad": "1998/12/03",
    "salma": "1988/06/19",
    "rim": "2001/02/15"
}

print("Bienvenue ! Vous pouvez consulter les anniversaires des personnes de la liste[span_3](start_span)[span_3](end_span).")
print("Personnes disponibles :", ", ".join(birthdays.keys()))
name_to_look = input("\nEntrez le nom de la personne dont vous voulez connaître l'anniversaire : ").strip()
birthday = birthdays.get(name_to_look)

if birthday:
    print(f"L'anniversaire de {name_to_look} est le {birthday}[span_6](start_span)[span_6](end_span).")
else:
    print(f"Désolé, nous n'avons pas l'anniversaire de '{name_to_look}' dans notre liste.")