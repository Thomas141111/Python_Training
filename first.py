def classify_temp(temp):
    if temp<0:
        return "Freezing"
    elif temp<10:
        return "Cold"
    elif temp<20:
        return "Cool"
    else:
        return "Hot"
    
temperature=int(input("Enter the temperature"))

temperature_category=classify_temp(temperature)
print(f"Temperature: {temperature} C, Category: {temperature_category}")
print("Temperature: ",temperature, "C, Category:" ,temperature_category)



