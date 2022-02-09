BirdCount = {"finch": 10, "myna": 15, "peacock": 15, "hornBill": 15}
# print(BirdCount)

# we use same value for many keys
# but for keys: must be unique


# Dictionary are mutable
dict1 = {
    0: "value for key is 0",
    1: "value for key is 1",
    "2": "value for key is 2 as string",
    (3, 4): "value for the key is (3,4) as a tuple",
    "Abhay": "abhay is in xi std"
}
# change value of existing key
# dict1["2"] = "abhay"
print(dict1)

# add new key and value in dir
dict1["abhay"] = "abhay is smart"
print(dict1)

dict1["alam"] = "he is also smart"