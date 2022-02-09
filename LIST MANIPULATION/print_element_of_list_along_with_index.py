l1 = ["Q", "W", "E", "R", "T", "Y"]
# here we store len() value in length variable
length = len(l1)
# with the help of for loop and membership operator we iterate the values in l variable
for a in range(length):
    # a store index and l[a] store value of it
    print("at index", a, "and", (a-length), "element is: ", l1[a])
