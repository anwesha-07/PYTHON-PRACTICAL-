cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    profit = sp - cp
    print("Seller made a profit of Rs.", profit)
elif cp > sp:
    loss = cp - sp
    print("Seller incurred a loss of Rs.", loss)
else:
    print("No profit, no loss.")
