employees=[]

while True:
    action=int(input("Choose an option:\n1.Add Employee\n2.Find Employee\n3.Remove Employee\n4.Exit\n"))
    if action==1:
        id=int(input("Enter empid: "))
        name=input("Enter employee name: ")
        emp=(id,name)
        employees.append(emp)
        print(employees)

    elif action==2:
        id=int(input("Enter empid: "))
        found = False
        for emp in employees:
            if emp[0]==id:
                print("Employee: ",emp)
                found = True
                break

        if not found:
            print("Record not found")

    elif action==3:
        id=int(input("Enter empid: "))
        found = False
        for emp in employees:
            if emp[0]==id:
                employees.pop(employees.index(emp))
                print("Sucess")
                found = True
                print(employees)
                break
        if not found:
            print("Record not found")

    elif action==4:
        print("Exited")
        break
    else:
        print("Wrong Input")
        break





