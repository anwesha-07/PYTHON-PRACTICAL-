c=0
while (True ):
    n = int(input("Enter a integer (Enter 0 or negative to stop): "))
    if n<=0 : 
        print("Total numbers processed:",c)
        break

    c+=1
    itr=0

    while n>9 :
        digit_sum = 0
        temp = n

        while temp!= 0 :
            rem = temp%10
            digit_sum += rem
            temp//=10
        
        n=digit_sum
        itr+=1

    print("Iterations:",itr,", Final digit: ",n)
