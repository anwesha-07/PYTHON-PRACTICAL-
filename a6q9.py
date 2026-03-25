str='Mca1stsem'.lower()
result={}
for ch in str:
    if ch in result:
        result[ch]+=1
    else:
        result[ch]=1
print(result)