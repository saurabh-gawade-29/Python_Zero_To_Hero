# TODO: id() is an inbuilt function in Python.
#  As we can see the function accepts a single parameter
#  and is used to return the identity of an object.
#  This identity has to be unique and constant
#  for this object during the lifetime.
#  Two objects with non-overlapping lifetimes may have the same id() value.

# Here we Create a Class
class Computer:
    pass

# Here we Create and object
c1 = Computer();
c2 = Computer();

# TODO: here we print address of the memory
print(id(c1))
print(id(c2))
print("address of memory is different:\n")
print("assign the memory using constructor:\n")
# Here we check python memory concept
str1 = "geek"
print(id(str1))
str2 = "geek"
print(id(str2))
# It will give true or false
print(id(str1) == id(str2))
