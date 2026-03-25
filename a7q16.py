def case_count(s):
    upper=0
    lower=0
    for i in s:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print("UPper Case:",upper)
    print("Lower Case:",lower)
case_count("AnweshASAHA")
