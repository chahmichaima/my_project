cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = [car.strip() for car in cars_string.split(",")]
print("Liste initiale :", cars_list)
print(f"Il y a {len(cars_list)} fabricants dans la liste[span_0](start_span)[span_0](end_span).")
cars_list_sorted_desc = sorted(cars_list, reverse=True)
print("Liste en ordre inverse (Z-A) :", cars_list_sorted_desc)
count_o = sum(1 for car in cars_list if 'o' in car.lower())
print(f"Nombre de fabricants contenant la lettre 'o' : {count_o}")
count_no_i = sum(1 for car in cars_list if 'i' not in car.lower())
print(f"Nombre de fabricants ne contenant pas la lettre 'i' : {count_no_i}")
# --- BONUS 1 ---
duplicates_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_cars = list(dict.fromkeys(duplicates_list))
formatted_string = ", ".join(unique_cars)
print(f"Entreprises sans doublons : {formatted_string}")
print(f"Nombre d'entreprises uniques : {len(unique_cars)}")

# --- BONUS 2 ---
sorted_asc = sorted(cars_list)
reversed_letters_list = [car[::-1] for car in sorted_asc]
print("Ordre A-Z avec noms inversés :", reversed_letters_list)