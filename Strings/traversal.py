# 4. Positive and Negative traversal
s=input("Enter a string : ")
for i in s:
    print(i)
for i in range(-1,-len(s),-1):
    print(s[i])


test_string ="Python Programming Pratice"
print("Original String",test_string)

print("1. First Character",test_string[0])
print("2.Last Character",test_string[-1])
print("3.Middle Character",test_string[int(len(test_string)/2)])
print("4.Character from Index 2 to 6")
for i in range(2,7):
    print (test_string[i])


test_string2="Python String Negative Indexing"
print("Accessing Characters from End")
print("Last Character",test_string2[-1])
print("Second Last Character",test_string2[-2])
print("Last Three: ")
for i in range(-1,-4,-1):
    print(test_string2[i])