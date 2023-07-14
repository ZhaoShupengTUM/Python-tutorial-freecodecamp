
employee_file = open("3-python-filesoperation/employees.txt", "r")  #r:read, w:write, a:append the file, r+:read and write the path is based on the root path of the work folder
print(employee_file.readable())
print("\n")
print(employee_file.read())
print(employee_file.readline()) #read only one line
print(employee_file.readlines())  #readlines: put each line inside a list

for employee in employee_file.readlines():
    print(employee)
employee_file.close()

employee_file = open("employees.txt", "a")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

employee_file = open("employees1.txt", "w")  #overwrite the file and create a file
employee_file.write("Kelly - Customer Service")
employee_file.close()


