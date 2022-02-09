a = (2, 3)
b = (2, 3)
check = a == b
print(check)

c = ("2", "3")
check1 = (a == c)
print(check1)

# Important:
d = (2.0, 3.0)
check2 = (a == d)
print(check2)
# Output: True

check3 = (a < d)
print(check3)
# Output: false

e = (2, 3, 4)
print(a < e)





