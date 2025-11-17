hundreds = int(input("Enter amount in hundreds: "))

amount = hundreds * 100

note100 = amount // 100
amount = amount % 100

note50 = amount // 50
amount = amount % 50

note10 = amount // 10

print("100-rupee notes =", note100)
print("50-rupee notes =", note50)
print("10-rupee notes =", note10)
