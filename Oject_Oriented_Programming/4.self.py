# Here we use: def functionName(self, parameter1, parameter2)
class Human:
    # TODO: instead of self we write a myObject here
    def __init__(myObject, name, age):
        myObject.name = name
        myObject.age = age

    def myFunction(abc):
        # here we not give a " , " symbol coz of string
        print("My name is:" +abc.name)

    def myAge(cde):
        # Here we give a " , " symbol for integer
        print("My age is:", + cde.age)

# Create a object
p1 = Human("saurabh", 24)
p1.myFunction()
p1.myAge()

# TODO: DO Comparison for better understanding
# TODO: Actual Code for self
class Person:
    def personMethod(self, firstName, lastName, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        print(f"my name is {firstName} {lastName} and my gender is {gender}")

# create object using constructor
person1 = Person()
person2 = Person()

person1.personMethod("Saurabh", "Gawade", "Male")
person2.personMethod("Komal", "Gawade", "Female")
