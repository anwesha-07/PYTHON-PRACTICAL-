s=[1,2,3,4]
result=[]
i=0
while i<len(s):
    new_list=s[:i]+s[i+1:]
    if new_list not in result:
        result.append(new_list)
    i+=1
print("New generated list is:",result)
