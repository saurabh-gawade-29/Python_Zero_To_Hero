num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

min = mid = max = None  # None operator  0

if(num1 < num2) and (num1 < num3):
    if(num2 < num3):
        min, mid, max = num1, num2, num3
    else:
        min, mid, max = num1, num3, num2
elif(num2 < num1) and (num2 < num3):
    if(num1 < num3):
        min, mid, max = num2, num1, num3
    else:
        min, mid, max = num2, num3, num1
else:
    if(num1 < num2):
        min, mid, max = num3, num1, num2
    else:
        min, mid, max = num3, num2, num1
print("Numbers in Ascending Order: ", min, mid, max)
