# Joining Tuple
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t = t1 + t2
# Concatenate 2 Tuple
# print(t)

# Output:(1, 2, 3, 4, 5, 6)

# You will get error for following
T = (1, 2, 3)
# newT = t + "abhay"
# add string

# newT = t + 1
# add number

# newT = t + "a"
# add char

# print(newT)
# ERROR: TypeError: can only concatenate tuple (not "str") to tuple

# IMPORTANT:

# variable = tuple + tuple_in_()


# NewT = t + (3)
# as int that's why error
# its Error to solve this
newT = t + (3, )
print(newT)









