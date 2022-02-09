names = ["saurabh", "abhay"]
# newName = names + "alam"
# we want to append "Alam" in list
# names.append("alam")
# print(names)

# # Updating elements in the list
# names[0] = "bhushan"
# print(names)

rollNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# remove element at index 5
del rollNumbers[5]

# 6 must be delete from list
print(rollNumbers)

# remove element as a slice
# del rollNumbers[0:2]
# print(rollNumbers)

# POP Method
rollNumbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove = rollNumbers2.pop()
print(remove)
# return : delete - store and print
# pop() does not contain any index : last element delete at this condition
# print(rollNumbers2)

rollNumbers2.pop(5)
# pop() contain index 5 that mean 5 value skip from it
print(rollNumbers2)

# # Diff POP and Del
# # del : remove single and slice of elements
# # pop : only remove single element
# # del : not return anything
# # pop : it return skip/pop/deleted value
#
