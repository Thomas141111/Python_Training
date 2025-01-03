from operator import countOf

# 1: Write a Python program group Similar items to Dictionary Values List
test_list=[4,6,6,4,2,2,4,8,5,8]
test_list.sort()
q1_result={}

for element in test_list:
    values=[]
    if element not in q1_result.keys():
        count=test_list.count(element)
        while count>0:
            values.append(element)
            count-=1
        q1_result[element]=values
print(q1_result)

# 2: Write a Python program convert List of Dictionaries to List of Lists Input:  [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}]
# Expected: [['Gfg', 'best'], [123, 10], [51, 7]]

input=[{"GFG":123,"Best":10},{"GFG":51,"Best":7},{"III":22,"DDD":21}]

q2_result=[]
duplicates=[]
for element in input:
    keys=list(element.keys())
    if duplicates.count(keys)==0:
        duplicates=[keys]
        q2_result.append(duplicates)
    q2_result.append(list(element.values()))

print(q2_result)




# 3: Write a Python program to print all distinct values in a dictionary.

original_list = [{'V': 'S001'},{'V': 'S002'},{'VI': 'S001'},{'VI': 'S005'},{'VII': 'S005'},{'V': 'S009'},{'VIII': 'S007'}]

unique_values = set()

for dictionary in original_list:
    for value in dictionary.values():
        unique_values.add(value)

print("Unique Values:", unique_values)

# 4: Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
my_dict={'a':200,'b':5874,'c':560,"d":1,"e":21}
top_keys=sorted(my_dict,key=my_dict.get,reverse=True)
q4_result=[top_keys[0:3]]
print(q4_result)


# 5: Write a Python program to combine values in a list of dictionaries.
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
q5_result={}
for item in item_list:
    item_name = item['item']
    amount = item['amount']

    if item_name in q5_result:
        q5_result[item_name] += amount
    else:
        q5_result[item_name] = amount
print(q5_result)

# 6: Write a Python program to sort a list alphabetically in a dictionary.

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for key,values in num.items():
    values.sort()
print(num)


# 7: Write a Python program to count the number of items in a dictionary value that is a list.
dict_7 ={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2'],'Tom':['subj1','subj2']}
total_len=0
for value in dict_7.values():
    total_len+=len(values)
print(total_len)

# 8: Write a Python program remove duplicate values across Dictionary Values

dict_8= {'first': [1, 4, 5, 6], 'sec': [1, 8, 9], 'third': [10, 22, 4], 'fourth': [5, 11, 22]}
all_values=[]
for value in dict_8.values():
    all_values.extend(value)
count_values={}

for value_1 in all_values:
    count_values[value_1]=all_values.count(value_1)
result_dict_8 = {}

for key, value_list in dict_8.items():
    unique_values = [value for value in value_list if count_values[value] == 1]
    result_dict_8[key] = unique_values
print(result_dict_8)


# 9: Write a Python program counting the frequencies in a list using dictionary in Python

input_9=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
result_9={}
for item in input_9:
    if item in result_9.keys():
        result_9[item]+=1
    else:
        result_9[item]=1
print(result_9)
