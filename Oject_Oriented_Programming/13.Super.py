class A:
    # Constructor
    def __init__(self):
        print("__init__ of A")

    def feature1(self):
        print("feature 1 of A")

    def feature2(self):
        print("feature 2 of A")


class B(A):
    # Constructor
    def __init__(self):

        # TODO: Super: Direct call constructor of parent
        super().__init__()

        print("__init__ of B")

    def feature3(self):
        print("feature 3 of B")

    def feature4(self):
        print("feature 4 of B")


# b1 is a object of class B
b1 = B()

# both constructor call here
# Run: coz constructor of class call automatically when object is created
