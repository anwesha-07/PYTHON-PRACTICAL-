l=[10,20,30,40,50]
k=2
result=[]
for i in range(len(l)-k+1):
    window=l[i:i+k]

    avg=sum(window)/k
    var=0
    for x in window:
        var=var+(x-avg)**2
    var=var/k
    result.append((avg,var))
print(result)

    
