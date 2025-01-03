# 2 Calculating shipping costs 

destination = int(input("Enter destination type[1.Domestic/2.International]"))
weight= int(input("Enter the weight in grams :"))

if(destination==1):
    if weight<1000:
        cost=500
    elif 1000<weight<5000:
        cost=1000
    else:
        cost=2500
elif(destination==2):
    if weight<1000:
        cost=1500
    elif 1000<weight<5000:
        cost=2500
    else:
        cost=5000

print("The cost is: ",cost)