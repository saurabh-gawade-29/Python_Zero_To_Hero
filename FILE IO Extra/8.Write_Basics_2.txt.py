# TODO: "w" - Write - will overwrite any existing content
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())


# Actual Content on file demofile3.txt
# this content is delete when 8.Write basics 2 run


# TODO: Note: the "w" method will overwrite the entire file.