def hcf(a,b):
    small=min(a,b)
    for i in range(small,0,-1):
        if a%i==0 and b%i==0:
            return i
print("HCF:",hcf(12,18))
