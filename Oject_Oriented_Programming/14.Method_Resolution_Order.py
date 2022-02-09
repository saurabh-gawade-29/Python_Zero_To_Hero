class A:
    # Constructor
    def __init__(self):
        print("Constructor of A")

    def feature1(self):
        print("feature 1 of A")

    def feature2(self):
        print("feature 2 of A")


class B:
    # Constructor
    def __init__(self):
        print("Constructor of B")

    def feature3(self):
        print("feature 3 of B")

    def feature4(self):
        print("feature 4 of B")

# TODO: class C(A,B) : As per MRO Left side is count as a main parent
class C(A,B):
    def __init__(self):
        # TODO: class A and B is parent:
        # TODO: Which constructor is called?
        # TODO: AS Per MRO Constructor of parent A is called
        super().__init__()
        print("Constructor of C")

    def feature5(self):
        print("feature 5 of C")


# b1 is a object of class B
c1 = C()
# TODO: As Per MRO constructor of A and C is call here
# Run: coz constructor of class call automatically when object is created
