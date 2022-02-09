rollNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new = list(rollNumbers)
print(new)
# its not make any new list with the name of "new" name
# too understand this see below changes
# rollNumbers[5] = "saurabh"
# print(rollNumbers)
# print(new)

# see the output : changes in both list,
# python consist as a same list

# see its a problem
# how we deal with it

# ans:
rollNumbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list method/function
# b = rollNumbers2
# OR
b = list(rollNumbers2)

rollNumbers2[5] = "Saurabh"
print(rollNumbers2)
print(b)

