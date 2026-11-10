from ex3 import Family
class TheIncredibles(Family):
    def __init__(self, last_name, members=None):
        if members is None:
            members = [
                {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
                {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperSarah'}
            ]
        super().__init__(last_name, members)
    def use_power(self):
        for member in self.members:
            if member['age'] > 18:
                print(f"{member['name']}'s power is: {member['power']}")
            else:
                print(f"{member['name']} is not old enough to use their power!")
    def incredible_presentation(self):
        print("\n* Here is our powerful family *")
        super().family_presentation()
        print("Incredible Superpowers:")
        for member in self.members:
            print(f"- {member['incredible_name']} -> Power: {member['power']}")
incredibles_family = TheIncredibles("Incredibles")
incredibles_family.incredible_presentation()
incredibles_family.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='JackJack')
incredibles_family.incredible_presentation()
print("\n--- Testing Powers ---")
incredibles_family.use_power()