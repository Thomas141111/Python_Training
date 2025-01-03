employees = {}
id = 101
while True:
    choice = int(input("Enter your choice:\n1.Add Add Employee\n2.Display Employees\n3.Show Employee Department wise\n4.Search Employee By Name\n"))

    if choice == 1:
        employe_name = input("Enter Employee Name: ").lower()
        employe_dep = input("Enter Employee Department: ").lower()
        employe_profile = input("Enter Employee profile: ").lower()
        employees[id] = {"Name": employe_name, "Department": employe_dep, "Profile": employe_profile}
        print("Employee Added Successfully")
        id += 1
        print(employees)

    elif choice == 2:
        for key, value in employees.items():
            print(f"Employee Name: {value['Name']}\nDepartment: {value["Department"]}\nProfile:{value["Profile"]}\n")

    elif choice == 3:
        dep = input("Enter Department: ").lower()
        for val in employees:
            if employees[val]['Department'] == dep:
                print(f"Employee Name: {employees[val]['Name']}\n")

    elif choice == 4:
        name = input("Enter name : ").lower()
        for val in employees:
            if employees[val]['Name'] == name:
                print("Employee Found")
                print(f"Employee Name: {employees[val]['Name']}")

    elif choice == 5:
        print(employees)
        continue
    else:
        print("Exited")
        break
