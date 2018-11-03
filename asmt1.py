emp = input("Enter Employee Name: ")
dig = input("Enter Designation: ")
sal = int(input("Enter Salary: "))
print("-------------------------------------------------------------------")
if dig == "manager" :
    print("Employee Name:",emp),
    print("Employee Designation:",dig),
    print("Employee Salary:",sal)
    print("Employee Bonus:",(sal/100)*20)

elif dig == "analyst":
    print("Employee Name:", emp),
    print("Employee Designation:", dig),
    print("Employee Salary:", sal)
    print("Employee Bonus:", (sal / 100) * 10)

elif dig == "clerk":
    print("Employee Name:", emp),
    print("Employee Designation:", dig),
    print("Employee Salary:", sal)
    print("Employee Bonus:", (sal / 100) * 5)