s1=input("Enter a string:")
s2=input("Enter a string:")
i=0
j=len(s2)-1
r=''
while i<len(s1) and j>=0:
    r+=s1[i]
    r+=s2[j]
    i+=1
    j-=1
if i<len(s1):
    r+=s1[i:]
if j>=0:
    r+=s2[:j+1][::-1]
    j-=1
print("New created string:",r)
