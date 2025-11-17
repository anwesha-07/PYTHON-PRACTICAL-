# MCA Admission Eligibility Checker

graduate = input("Are you a graduate? (yes/no): ").lower()
category = input("Enter category (GEN/SC/ST): ").upper()
grad_marks = float(input("Enter graduation percentage: "))
math_marks = float(input("Enter Mathematics percentage (in 10+2 or graduation): "))

if graduate == "yes":
    if category == "SC" or category == "ST":
        if grad_marks >= 45 and math_marks >= 50:
            print("Eligible for MCA admission.")
        else:
            print("Not eligible for MCA admission.")
    else:
        if grad_marks >= 50 and math_marks >= 50:
            print("Eligible for MCA admission.")
        else:
            print("Not eligible for MCA admission.")
else:
    print("Not eligible for MCA admission.")
