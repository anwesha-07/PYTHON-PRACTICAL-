days = int(input("Enter number of days late: "))

if days <= 5:
    print("Fine: Rs.", days * 0.50)
elif days <= 10:
    print("Fine: Rs.", (5 * 0.50) + (days - 5) * 1)
elif days <= 30:
    print("Fine: Rs.", (5 * 0.50) + (5 * 1) + (days - 10) * 5)
else:
    print("Your membership is cancelled.")
