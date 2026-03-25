id=[1,2,3,4,]
name=['Anwesha','Dev','Ankita','Basu']
marks=[90,95,92,95]
dic={}
for i in range(len(id)):
    dic[id[i]]={name[i]:marks[i]}
print(dic)
