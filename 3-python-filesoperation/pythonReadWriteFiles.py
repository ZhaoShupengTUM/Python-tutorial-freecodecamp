employee_file = open("employees.txt", "r")  #r:read, w:write, a:append the file, r+:read and write
print(employee_file.readable())
print("\n")
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readlines()[1])  #readlines: put each line inside a list
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

employee_file = open("employees.txt", "a")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

employee_file = open("employees1.txt", "w")  #overwrite the file and create a file
employee_file.write("Kelly - Customer Service")
employee_file.close()


