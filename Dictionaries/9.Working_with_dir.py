# init the dictionary

emp = {"name": "saurabh", "salary": 10000, "age": 23}
# print(emp)

# creating a empty dir with dict()
# employee = dict()
# print(employee)

# add value to empty dict
# important
# employee = dict(name='saurabh', salary=10000, age=23)
# print(employee)

# make keys string as a type
employee = dict(zip(('name', 'salary', 'age'),('saurabh', 10000, 23)))
print(employee)
