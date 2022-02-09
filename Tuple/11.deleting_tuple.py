# del statement
# tuples are immutable
# so with the help of del you cannot delete single value of tuple

t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# del t[1]
# print(t)

# TypeError: 'tuple' object doesn't support item deletion
# but you can delete whole tuple using del

del t
print(t)

# empty  () this is not possible
# delete
# NameError: name 't' is not defined
# that means you successfully delete whole tuple
