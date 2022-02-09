ch = input("Enter single Charchter: ")

if(ch >= "A") and (ch <= "Z"):  # A-Z
    print("You entered an upper case charchter.")
elif (ch >= "a") and (ch <= "z"):  # a-z
    print("You entered an lower case charchter.")
elif (ch >= "0") and (ch <= "9"):  # 0-9
    print("You entered a digit.")
else:
    print("You entered a special charchter")  # msg - String
