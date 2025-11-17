health = input("Enter health (excellent/poor): ").lower()
age = int(input("Enter age: "))
location = input("Enter location (city/village): ").lower()
sex = input("Enter sex (male/female): ").lower()
policy_amount=int(input("Enter your policy amount:"))

if health == "excellent" and 25 <= age <= 35 and location == "city":
    if sex == "male":
        print("Insured")
        print("Premium rate: Rs.",(policy_amount/1000)*4)
        print("Maximum policy amount: Rs. 2,00,000")
    elif sex == "female":
        print("Insured")
        print("Premium rate: Rs.",(policy_amount/1000)*3)
        print("Maximum policy amount: Rs. 1,00,000")
    else:
        print("Not insured")
elif health == "poor" and 25 <= age <= 35 and location == "village" and sex == "male":
    print("Insured")
    print("Premium rate: Rs.",(policy_amount/1000)*6)
    print("Maximum policy amount: Rs. 10,000")
else:
    print("Not insured")
