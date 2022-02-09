emp = {"john": {"age": 25, "salary": 20000}, "divya": {"age": 35, "salary": 50000}}
for key in emp:
    print("employee", key, ":")
    print('age:', str(emp[key]["age"]))
    print("salary:", str(emp[key]["salary"]))
