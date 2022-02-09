names = ["saurabh", "abhay", "alam", "bhushan", "shubham"]

# index method
# index(value) = its gives index as per value
# index = names.index("alam")
# print(index)

# Append Method
# add the element at end of the list
# names.append("sam")
# print(names)

# extend method
# append list with another list
# rollNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# newRollNumber = [11, 12]
# rollNumbers.extend(newRollNumber)
# print(rollNumbers)
# # its cannot change another list which we want to extend
# print(newRollNumber)


# diff append() and extend()
# append: add one element at a time in list
# extend: add multiple element at a time in list

# insert Method
# we can add element in list anywhere using index
# t1 = ["a", "e", "o", "u"]
# # "i" is missing in vowels
# t1.insert(2, "i")
# print(t1)

# # Pop Method
# rollNumbers3 = [1, 2, 3, 4, 5]
# popElementNoIndex = rollNumbers3.pop()
# print("pop element without index is: ", popElementNoIndex)
#
# # if we cannot pass index in pop() it will pop out last element
# print(rollNumbers3)
#
# popElement = rollNumbers3.pop(0)
# print("POP element will be: ", popElement)

# Remove Method
# remove() methods remove the first occurrence  of given list
# t2 = ["a", "b", "c", "d", "a", "a", "a"]
# t2.remove("a")
# print(t2)

# clear Method
# clear all the element form the list
# t3 = [1, 2, 3, 4, 5]
# print("before Clear Method", t3)
# t3.clear()
# print("after Clear Method", t3)

# The Count Method
# return as well
# t4 = [13, 18, 20, 18, 50]
# count1 = t4.count(18)
# print(count1)
# count2 = t4.count(40)
# print(count2)


# reverse Method
# t5 = [1, 2, 3, 4, 5]
# t5.reverse()
# print("After Reverse Method: ", t5)

# sort Method
# t6 = ["d", "c", "b", "a"]
# t6.sort()
# print("After Sort Method", t6)

# actually it does not return anything
