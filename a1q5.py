num = int(input("Enter a 5-digit number: "))

d1 = num // 10000
d2 = (num // 1000) % 10
d3 = (num // 100) % 10
d4 = (num // 10) % 10
d5 = num % 10

d1 = (d1 + 1) % 10
d2 = (d2 + 1) % 10
d3 = (d3 + 1) % 10
d4 = (d4 + 1) % 10
d5 = (d5 + 1) % 10

new_num = d1*10000 + d2*1000 + d3*100 + d4*10 + d5

print("New number =", new_num)
