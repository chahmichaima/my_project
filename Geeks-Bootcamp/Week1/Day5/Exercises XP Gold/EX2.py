import random
class MyList:
    def __init__(self, letters):
        self.mylist = letters
    def get_reversed(self):
        return list(reversed(self.mylist))
    def get_sorted(self):
        return sorted(self.mylist)
    def generate_random_list(self):
        return [random.randint(1, 100) for _ in range(len(self.mylist))]
l = MyList(['b', 'a', 'd', 'c'])
print("Originale :", l.mylist)
print("Inversée :", l.get_reversed())
print("Triée :", l.get_sorted())
print("Bonus (aléatoire) :", l.generate_random_list())