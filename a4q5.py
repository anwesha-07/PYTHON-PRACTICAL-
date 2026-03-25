words=["eat","tea","tan","ate","nat","bat"]
group={}

for word in words:
    key="".join(sorted(word))
    if key not in group:
        group[key]=[]
    group[key].append(word)

result=list(group.values())
print(result)
