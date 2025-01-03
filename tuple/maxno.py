l = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

maximum = l[0]
for i in range(len(l)):
    if maximum < l[i]:
        maximum = l[i]
print(maximum)

print("simple:- " + str(max(l)))