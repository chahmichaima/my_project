#Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
#Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers

import random

def compare_with_random(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print(f"Succès ! Les deux nombres sont identiques : {user_number}[span_1](start_span)[span_1](end_span)")
    else:
        print(f"Échec ! Les nombres sont différents[span_2](start_span)[span_2](end_span). Ton nombre : {user_number}, Nombre aléatoire : {random_number}[span_3](start_span)[span_3](end_span)")
compare_with_random(45)