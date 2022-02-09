# Multiple Inheritance
class A:

    def feature1(self):
        print("feature1")

    def feature2(self):
        print("feature2")


class B:

    def feature3(self):
        print("feature3")

    def feature4(self):
        print("feature4")


class C(A,B):

    def feature5(self):
        print("feature5")


# Object Creation
c1 = C()
# C can  access all the properties from A and B
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()