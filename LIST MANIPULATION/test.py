# s1 = int(input("enter marks of student1: "))
# s2 = int(input("enter marks of student2: "))
# s3 = int(input("enter marks of student3: "))
# s4 = int(input("enter marks of student4: "))
# s5 = int(input("enter marks of student5: "))
# s6 = int(input("enter marks of student6: "))
#
# marks = [s1, s2, s3, s4, s5, s6]
# print(marks)
# marks.sort()
# # does not return anything
# # only sorting
# print(marks)

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print(" Factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
