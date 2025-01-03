# 1
s="abababa"
result=""
for i in s:
    if i in result:
        pass
    else:
        result=result+i
print(result)

# 2

def count_char(char,string):
    count1=0
    for i in string:
        if char==i:
            count1=count1+1
    return count1

s="miiiisssspp"
s2=""
for i in s:
    if i in s2:
        pass
    else:
        s2=s2+i

for j in s2:
    count= count_char(j,s)
    print("count for ",j,"is ",count)

# 3
s="Duugu khushi sulabh"
l=s.split()
l.reverse()
result2=""
for i in l:
    result2=result2+i+" "
print(result2)
