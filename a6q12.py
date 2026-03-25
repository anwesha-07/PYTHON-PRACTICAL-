d1={'key1':1,'key2':2,'key3':3}
d2={'key1':1,'key3':3}
for key in d1:
    if key in d2 and d1[key]==d2[key]:
        print(f"{key}:{d1[key]} is present in both")