# # len() Method
# emp = {'name': 'saurabh', 'age': 23, 'salary': 10000}
# a = len(emp)
# print("the length before new entry", a)
#
# # now we add new entry into dir
# emp['new'] = 'sales'
# print("after add new entry", emp)
# print("the length after new entry", len(emp))

# # clear() Method
# # it's not delete the dir its just delete all the elements in the dir
# clearDir = {'name': 'saurabh', 'age': 23, 'salary': 10000}
# clearDir.clear()
# print("After used clear() method", clearDir)

# get() Method
# it's written value for key and
# if there is no key present in the dir it will throw a error

# getDir = {'name': 'saurabh', 'age': 23, 'salary': 10000}
# print("get value using getMethod", getDir.get('salary'))
#
# print(getDir.get('abhay'))
# it will not give a error.
# abhay is not defined

# items() Method
# this method returns all the items in dir as a sequence of(key:value) tuple
# save the value in tuple

# employee = {'name': 'saurabh', 'age': 23, 'salary': 10000}
# myList = employee.items()
# for x in myList:
#     print(x)

# # Keys() method
# emp1 = {'name': 'saurabh', 'age': 23, 'salary': 10000}
# keys = emp1.keys()
# print(keys)
#
# # values() method
# emp1 = {'name': 'saurabh', 'age': 23, 'salary': 10000}
# values = emp1.values()
# print(values)

# update() method
# oldEmp = {'name': 'saurabh', 'age': 23, 'salary': 10000}
# newEmp = {'name': 'bhushan', 'age': 24, 'salary': 20000}
# oldEmp.update(newEmp)
# print(oldEmp)
# print(newEmp)