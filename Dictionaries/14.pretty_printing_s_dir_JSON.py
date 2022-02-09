# JSON : JavaScript Object Notation
# it's a standard text based format for representing structure data based on JS object syntax.
# Its used for transmitting data in web application

# first  print()
import json

win = {"saurabh": 3, "abhay": 5, "alam": 7}
print(win)

# now use pretty printing
print(json.dumps(win, indent=5))


