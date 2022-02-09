s = {1, 8, 2, 3, 1}
print(s)
# its show "1" => once

# length of set S
print(len(s))

# remove method
s.remove(8)
print(s)

# pop method = remove last element from set
s.pop()
print(s)

# Union method:
s.union({8, 11})
print(s)

# Intersection Method
s.intersection({8, 11})
print(s)

# clear method = remove all the element from set and show op as a empty set
s.clear()
print(s)


