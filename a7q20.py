def is_perfect(n):
    sum_div=0
    for i in range(1,n):
        if n%i==0:
            sum_div+=i
    if sum_div==n:
        print("PERFECT")
    else:
        print("NOT PERFECT")
is_perfect(6)
