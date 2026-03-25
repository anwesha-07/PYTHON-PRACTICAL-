d1={1:10,2:20,4:6}
d2={3:30,4:40,5:2}
d3={5:50,6:60}
result={}
for d in (d1,d2,d3):
    for key,value in d.items():
        if key in result:
            result[key]+=value
        else:
            result[key]=value
print(result)