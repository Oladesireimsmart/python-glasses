
class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye Color:", self.eye_color)
        print("Height (cm):", self.height_cm1)


class Child(FamilyMember):


    def __init__(self, name, age, eye_color, height_cm):
        super().__init__(eye_color, height_cm)
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)

    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()


    def favorite_hobby(self, hobby):
        print(self.name, "loves", hobby)


Child = Child("Alice", 10, "Blue", 140)


Child.show_traits()
Child.favorite_hobby("painting")


print("is Kid a subclass of FamilyMember?", issubclass(Child, FamilyMember))
