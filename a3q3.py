n= int(input(" enter length: "))
i=0
a=" "
while(i<n):
	num=int(input("enter number:"))
	if i%2==0 and num%2==0:
			a=a+" "+str(num)
	elif i%2!=0 and num%2!=0:
			a=a+" "+str(num)
	else:
		i+=1
		continue
	i+=1
print(a)