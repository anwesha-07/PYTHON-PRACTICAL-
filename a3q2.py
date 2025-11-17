n= int(input("enter the total values: "))
k = int(input("enter the value of multiplier"))
i=0
a=""
while(i<n):
	num=int(input("enter values: "))
	if i!=0 and num%k==0:
		a=a+" "+str(num)
	i+=1
print(a)
