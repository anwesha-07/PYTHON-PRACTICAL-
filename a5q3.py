a=[1,2,3,4,5]
b=[10,20,30,40,50]
k=2
result=[]
newa=a[-k:]+a[:-k]
for i in range(len(newa)):
    result.append(newa[i]+b[i])
print(newa)
print(result)
