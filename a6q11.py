d1={'dress':23,'pant':45,'shoe':12,'bangle':55,'book':8}
items=list(d1.items())
n=len(items)
for i in range(n):
    for j in range(i+1,n):
        if items[i][1]<items[j][1]:
            items[i],items[j]=items[j],items[i]
for i in range(3):
    print(items[i][0],items[i][1])