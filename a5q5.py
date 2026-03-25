l=[1,3,5,4,2,1,2,3,2]
n=len(l)
long=[]
for i in range(1,n-1):
    if l[i-1]<l[i]>l[i+1]:
        left=i-1
        right=i+1
        while left>0 and l[left-1]<l[left]:
            left=left-1
        while right<n-1 and l[right]>l[right+1]:
            right=right+1
        peak=l[left:right+1]

        if len(peak)>len(long):
             long=peak
if long:
    print("Subsequence:",long)
    print("length",len(long))
else:
    print("None")
