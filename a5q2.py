sales=[[5,3,0,2],
       [7,0,2,1],
       [0,1,4,0]
]
result=[]
for col in range(len(sales[0])):
    total=0
    for row in range(len(sales)):
        total=total+sales[row][col]
    result.append(total)
print("Total Sale of product 1:",result[0])
print("Total Sale of product 2:",result[1])
print("Total Sale of product 3:",result[2])
print("Total Sale of product 4",result[3])
max=max(result)
min=min(result)
for i in range(len(result)):
    if result[i]==max:
        print("Max saled product is:",i+1)
for i in range(len(result)):
    if result[i]==min:
        print("Min saled product is:",i+1)
