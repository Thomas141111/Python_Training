contacts={"Name":[],"Contact-No":[],"Email":[]}
while True:
    choice=int(input("Enter your choice:\n1.Add Contact\n2.Display Contacts\n3.Show Contact Details of user(name)\n4.Remove Contact(name)\n"))
    if choice==1:
        name=input("Enter name:")
        contact_no=int(input("Enter contact no:"))
        email=input("Enter email")

        contacts["Name"].append(name)
        contacts["Contact-No"].append(contact_no)
        contacts["Email"].append(email)

        print(contacts)
        continue

    if choice==2:
        for data in range(len(contacts["Name"])):
            print(f'Name:{contacts["Name"][data]} , Contact:{contacts["Contact-No"][data]} , Email:{contacts["Email"][data]}')
        continue

    if choice==3:
        name=input("Enter name:")
        if name in contacts["Name"]:
            index=contacts["Name"].index(name)
            print(f"Name:{contacts["Name"][index]}\nContact:{contacts["Contact-No"][index]}\nEmail:{contacts["Email"][index]}")
        else:
            print("No Record of user")
        continue

    elif choice==4:
        search_name=input("Enter Name :")
        if search_name in contacts["Name"]:
            index=contacts["Name"].index(search_name)
            del contacts["Name"][index]
            del contacts["Contact-No"][index]
            del contacts["Email"][index]
            print("Contact No is Deleted")
        else:
            print("Contact is not present")
        continue
    else:
        print("Exit the program:: ")
        break



