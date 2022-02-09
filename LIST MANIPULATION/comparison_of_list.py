l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = [1, [2, 3]]


# Check Equality for normal lists
ans = (l1 == l2)
# you can use round brackets as well
print(ans)
# True

# check Equality for nested list
ans2 = l3 == l1
print(ans2)
# false

# check which one is big list
ans3 = l1 < l2
print(ans3)
# false

# check above same for nested list
# ans4 = l1 < l3
# print(ans4)
# you will get error
# #TypeError: '<' not supported between instances of 'int' and 'list'

# Concatenation
l1 = ["Saurabh", "abhay"]
l2 = ["Gawade", "alam"]
l3 = l1 + l2
print(l3)

# !You will get error for below 2 example
# list + number
ListNumber = l1+2
print(ListNumber)

# list + string
ListString = l2+"abhay"
print(ListString)



