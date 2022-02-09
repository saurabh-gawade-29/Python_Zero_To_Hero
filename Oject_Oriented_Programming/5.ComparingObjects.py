class Person:

    def __init__(self):
        self.age = 25

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


# Create Object here
p1 = Person()
p2 = Person()

# Change the Value of p1 Object // we will do like this also
# p1.age = 25


# Update the value of age using update function created by us
p1.update()

# TODO: Comparing Object
# TODO: TRY
if p1 == p2:
    print("They are same")
# In above they compare address we dont want to compare objects

# TODO: So we need to try this
# Compare is not a built in method we need to create it
if p1.compare(p2):
    print("They are same")
else:
    print("They are not same")


print(p1.age)
print(p2.age)


