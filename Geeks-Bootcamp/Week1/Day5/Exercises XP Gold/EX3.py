class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]
    def add_item(self, name, price, spice, gluten):
        new_dish = {"name": name, "price": price, "spice": spice, "gluten": gluten}
        if new_dish not in self.menu:
            self.menu.append(new_dish)
            print(f"Le plat '{name}' a été ajouté au menu.")
        else:
            print(f"Le plat '{name}' existe déjà dans le menu.")
    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"Le plat '{name}' a été mis à jour avec succès.")
                return
        print(f"Erreur : Le plat '{name}' n'est pas dans le menu.")
    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"Le plat '{name}' a été supprimé.")
                print("Menu mis à jour :", self.menu)
                return
        print(f"Erreur : Le plat '{name}' n'est pas dans le menu.")
manager = MenuManager()
manager.add_item("Pizza", 20, "B", True)
manager.update_item("Soup", 12, "A", False)
manager.remove_item("Salad")