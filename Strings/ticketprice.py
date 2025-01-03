# 1 Calculate ticket price 
def ticket_price(age,time):
    children_std_price=100
    adult_std_price=200
    if age<18:
        if time<12:
            return children_std_price-50
        else :
            return children_std_price
    
    elif age>18:
        if time<12:
            return adult_std_price-150
        else:
            return adult_std_price
    elif age>60:
        return adult_std_price-70

age=int(input("Enter age :"))
time= input("Enter Time(daytime/night)")
price=ticket_price(age,time)

print("The price is: ",price)
