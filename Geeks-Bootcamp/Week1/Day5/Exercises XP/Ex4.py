from collections import defaultdict
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"L'animal '{new_animal}' a été ajouté au zoo.")
        else:
            print(f"L'animal '{new_animal}' est déjà présent dans le zoo.")
    def get_animals(self):
        print(f"Animaux du zoo ({self.name}) : {self.animals}")
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"L'animal '{animal_sold}' a été retiré du zoo.")
        else:
            print(f"L'animal '{animal_sold}' n'existe pas dans ce zoo.")
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_dict = defaultdict(list)
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            grouped_dict[first_letter].append(animal)
        return dict(grouped_dict)
    def get_groups(self):
        groups = self.sort_animals()
        for letter, group_animals in groups.items():
            if len(group_animals) == 1:
                print(f"{letter}: '{group_animals[0]}'")
            else:
                print(f"{letter}: {group_animals}")
new_york_zoo = Zoo("New York Zoo")
for animal in ["Ape", "Baboon", "Bear", "Cat", "Cougar", "Eel", "Emu", "Giraffe"]:
    new_york_zoo.add_animal(animal)
print("\n--- Affichage des groupes triés ---")
new_york_zoo.get_groups()