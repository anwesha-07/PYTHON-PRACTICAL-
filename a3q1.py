n=int(input("enter no. of item"))
sum_of_odd=0
sum_of_even=0
i=0
while(i<n):
    num=int(input("enter numbers: "))
    if num%2==0:
        sum_of_even+=num
    else:
        sum_of_odd+=num
    i+=1
print("sum of all even numbers:",sum_of_even)
print("sum of all odd numbers:",sum_of_odd)


