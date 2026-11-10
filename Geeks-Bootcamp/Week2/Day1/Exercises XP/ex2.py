class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return (self.weight / self.age) * 10
    def fight(self, other_dog):
        my_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        if my_score > other_score:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif my_score < other_score:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"The fight between {self.name} and {other_dog.name} is a draw!"
dog1 = Dog("Rex", 3, 25)
dog2 = Dog("Max", 5, 30)
dog3 = Dog("Rocky", 2, 15)
print("\n--- Exercise 2 Output ---")
print(dog1.bark())
print(f"{dog1.name}'s running speed: {dog1.run_speed()}")
print(dog2.bark())
print(f"{dog2.name}'s running speed: {dog2.run_speed()}")
print(dog1.fight(dog2))
print(dog3.fight(dog1))