ram = int(input("Enter Ram's age: "))
shyam = int(input("Enter Shyam's age: "))
ajay = int(input("Enter Ajay's age: "))

if ram < shyam and ram < ajay:
    print("Ram is the youngest.")
elif shyam < ram and shyam < ajay:
    print("Shyam is the youngest.")
else:
    print("Ajay is the youngest.")
