t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
slice1 = t1[3: -3]
# slice1 = t1[3:]
# slice1 = t1[3: 30]
# slice1 = t1[-30: 3]
# print(slice1)
# Output: (4, 5, 6)

# slice also support step value
t2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
# sl1 = t1[0:10:2]
sl2 = t1[::3]
# include every second element : that means skip 1 value
print(sl2)




