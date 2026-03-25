a=input("Enter a String").lower()
b=input("Enter another string").lower()
missing=[]
for ch in a:
    if ch not in b:
        missing.append(ch)
if len(missing)==0:
    print(True)
else:
    print(False)
    print("Missing characters:",missing)
