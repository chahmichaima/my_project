class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        if members is not None:
            self.members = members
        else:
            self.members = [
                {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
                {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
            ]
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the new born!")
    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] > 18
        return False
    def family_presentation(self):
        print(f"\nFamily Last Name: {self.last_name}")
        print("Members details:")
        for member in self.members:
            print(f"- Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")
my_family = Family("Smith")
my_family.family_presentation()
my_family.born(name='Jack', age=0, gender='Male', is_child=True)
print(f"Is Michael over 18? {my_family.is_18('Michael')}")
my_family.family_presentation()