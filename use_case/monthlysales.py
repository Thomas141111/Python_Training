monthly_sales=[2000,3000,2500,4000,3500,122,3321,442,111,34,11,444]
months=["jan","feb","mar","april","may","june","july","aug","sep","oct","nov","dec"]
print("The Monthly Sales is: ")
print(monthly_sales)

print("The total sales are: ")
print(sum(monthly_sales))

print("The average sales are: ")
print(int(sum(monthly_sales)/len(monthly_sales)))

print("The best month for sales")
index=monthly_sales.index(max(monthly_sales))
print(months[index])
