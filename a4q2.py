str=input("Enter a String:")
digit=[]
for ch in str:
    if '0'<=ch<='9':
        digit.append(int(ch))
if len(digit)==0:
    print("There is no digit available")
else:
    print("Digits:",digit)
    print("Total:",sum(digit))
    print("Minimum:",min(digit))
    print("Maximum:",max(digit))
    print("Average:",sum(digit)//len(digit))

