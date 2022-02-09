# there are two methods for delete elements from dir
d = {"salary": 100000, "age": 24, "name": "saurabh"}
print("before delete: ", d)
# with the help of Del function
# del d["salary"]
# print("after delete: ", d)

# if the key is not present in the dir
# del d["new"]
# print(d)

# Another method is pop() method
popValue = d.pop("age")
print(popValue)
print("The dir after using pop(): ", d)