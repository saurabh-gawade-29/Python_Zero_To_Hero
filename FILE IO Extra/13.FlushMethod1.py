"""
In the below program,
in reading mode then the flush() method
only clears the internal buffer of the file,
it does not affect the content of the file. So, the contents of the file can be read and displayed.
"""

# opening the file in read mode
fileObject = open("flush.txt", "r")

# clearing the input buffer
fileObject.flush()

# reading the content of the file
fileContent = fileObject.read()

# displaying the content of the file
print(fileContent)

# closing the file
fileObject.close()