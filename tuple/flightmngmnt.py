flights=[]

while True:
    action = int(input("Choose an option:\n1.Add Flight\n2.Find Flight\n3.Remove Flight\n4.Exit\n"))
    if action==1:
        no=int(input("Enter the FlightNo:"))
        city=input("Enter the City:")
        time=input("Enter the time:")

        flight=(no,city,time)
        flights.append(flight)

        print(flights)

    elif action==2:
        id=int(input("Enter flight No: "))
        found=False
        for flight in flights:
            if flight[0]==id:
                print("Flight: ",flight)
                found = True
                break
        if not found:
            print("Record not found")


    elif action==3:
        flight_no=int(input("Enter flight no to be deleted: "))
        found = False
        for flight in flights:
            if flight[0]==flight_no:
                flights.pop(flights.index(flight_no))
                found = True
                print(flights)
                break
        if not found:
            print("Record not found")

    elif action==4:
        print("Exited")
        break
    else:
        print("Wrong Input")
        break



