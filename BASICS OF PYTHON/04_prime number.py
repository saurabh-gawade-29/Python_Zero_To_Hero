a = int(input("enter a number:"))
num = int(a/2)+1
for i in range(2, num):
    rem = a % i
    if (rem == 0):
        print("its not a prime number")
        break
    else:
        print("its a prime number")
