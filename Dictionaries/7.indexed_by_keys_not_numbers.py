dict1 = {
    0: "value for key is 0",
    1: "value for key is 1",
    "2": "value for key is 2 as string",
    (3, 4): "value for the key is (3,4) as a tuple"
}

value1 = dict1[0]
print(value1)

value2 = dict1[1]
print(value2)

value3 = dict1["2"]
print(value3)

value4 = dict1[3, 4]
print(value4)