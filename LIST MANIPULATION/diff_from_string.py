vowel = ["a", "e", "i", "o", "u"]
# string is immutable (we do not change the string char)

# while => list are mutable (we can change the list items)
# here we want to see the list item

# vowel = "A" # overwrite

vowel[0] = "A"
vowel[-1] = "U"
print(vowel)

# vowel[0] = "A"
# # here i change the list item at zero index
# vowel[-1] = "U"
# # here i change the list item at -4 index
# print(vowel)


