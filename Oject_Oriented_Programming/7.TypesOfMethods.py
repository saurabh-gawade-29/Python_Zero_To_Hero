class Car:

    # Class Variable:
    # TODO:class variables are defined within class
    # TODO: Scope for all methods
    wheels = 4

    def __init__(self):
        # Instance variable
        #TODO:instance variables are defined within methods
        # TODO: Scope within method
        self.mileage = 10
        self.company = "BMW"

    @classmethod
    def test(cls):
        return Car.wheels

    @staticmethod
    def check():
        return "not a class method nor instance method which is static method"


# Object Creation
c1 = Car()
c2 = Car()

# str and int object is not callable error coz
# TODO: you use integer as a function
# Wrong way ^--^
# TODO: We need to call method using object eg. c1.__init__(self)
# c1.mileage()
# c1.company()

print(f"Car is give mileage {c1.mileage} and company is {c1.company}")
print(f"wheels is {c1.wheels} and you can call like this using classname.variable {Car.wheels}")
print(f"number of wheels of car from another method:{c1.test()}")
print(c2.check())