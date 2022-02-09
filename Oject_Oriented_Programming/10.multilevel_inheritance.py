# Single Inheritance
# TODO: parent -> Child
class A:

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")


class B(A):

    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")


class C(B):

    def feature5(self):
        print("feature 5")

    def feature6(self):
        print("feature 6")


# Object creation
a1 = A()
b1 = B()
c1 = C()

# When we not use single inheritance : CLASS B(A)
a1.feature1()
a1.feature2()

b1.feature3()
b1.feature4()

# After: B can access all properties of A
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

# After Multilevel Inhertiance
# C can access all the properties from A and B

c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()