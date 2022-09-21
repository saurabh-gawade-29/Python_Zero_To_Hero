import os

if os.path.exists("needDelete2.txt"):
    os.remove("needDelete2.txt")
else:
    print("The file does not exist")

    # TODO: Rename file in line number 2,3
