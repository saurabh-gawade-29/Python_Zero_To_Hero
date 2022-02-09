name = "SAURABH"
print(name[0])  # print 0 index value which is S
print(name[1])  # print 1 index value which is A

# Now we Do Slicing based on Indexing

print(name[0:5])
# expected Output will be: SAURAB
# BUT the actual output will be SAURA

print(name[:5])
# what is black value?
# Blank Value will be:

print(name[1:])
# what is blank value will be


# Why Negative Indexing???
# You dont know the length of string: AND you want to find last Alphabet

print(name[-1])
# output will be:H


# Now slice using Negative index
print(name[-4:-1])  # it will take as [3:6]
# o/p: RAB


# SLicing with skip value
print(name[0:6:2])
# here start index 0 and end index 6 and 2 is skiping value
# 2 is skip value that means skip 2 value after every print charachter
# _S A _U R _A B H


# NOW FIND LENGTH OF STRING
print(len(name))
# 0-6 = 7
