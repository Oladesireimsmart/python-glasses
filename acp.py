
class pet:
    def __init__(self, name,animal, age):
        self.name = name
        self.animal = animal
        self.age = age

    def show_pet(self):
        print("The name of the pet is:", self.name)
        print("The type of animal is:", self.animal)
        print("The age of the pet is:", self.age)

    

pet1 = pet("Buddy", "Dog", 3)


pet1.show_pet()

