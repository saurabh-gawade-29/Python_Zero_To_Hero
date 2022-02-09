aList = ["15", "6", "13", "22", "3", "52", "2", "a"]
print("Original List: ", aList)
# As its is list
n = len(aList)
# 8
for i in range(n):
    for j in range(0, n-i-1):
        if aList[j] > aList[j+1]:
            aList[j], aList[j+1] = aList[j+1], aList[j]
print("list after sorting:", aList)
