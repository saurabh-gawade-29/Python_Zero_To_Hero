# Outer class
class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        # TODO: Object of inner class (inside main class)
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    # Inner Class
    class Laptop:

        def __init__(self):
            self.model = "hp"
            self.processor = "i5"
            self.ram = "16gb"

        def show(self):
            print(self.model, self.processor, self.ram)


# TODO: Object of inner class (Outside main class)
# lap1 = Student.Laptop()

# object creation
student1 = Student('saurabh', 1)
student2 = Student('komal', 2)

student1.show()
student2.show()

