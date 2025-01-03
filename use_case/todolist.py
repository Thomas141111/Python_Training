todo_list=[]
while True:
    option=int(input("Enter option \n 1.Add\n2.Update\n3.Delete\n4.Exit\n"))
    if option==1:
        value=input("Enter the activity: ")
        todo_list.append(value)
        print(todo_list)
    elif option==2:
        value=int(input("Enter the activity to update: "))
        value_2=input("Enter the activity: ")
        todo_list.pop(value)
        todo_list.insert(value,value_2)
        print(todo_list)
    elif option==3:
        value=int(input("Enter the task to delete"))
        todo_list.pop(value)
        print(todo_list)
    elif option==4:
        break
    else:
        print("Invalid Input")
        break
