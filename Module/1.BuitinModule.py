import platform

x = dir(platform)
print(x) #! Here you get list of platform information
print(type(x)); #TODO: Your can check type here

#! In Platform Module there are some built in method in that
y = platform.system()
print(y)

#! There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
z = dir(platform)
print(z)