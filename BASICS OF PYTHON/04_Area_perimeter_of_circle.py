radius = float(input("Enter Radius: "))
print("1: Calculate Area")
print("2: Calculate perimeter")
choice = int(input("Enter your choice (1 or 2): "))
if (choice == 1):
    area = 3.1495*radius*radius
    print(area)
elif(choice == 2):
    perimeter = 2*3.1495*radius
    print(perimeter)
else:
    print("please select 1 OR 2")
