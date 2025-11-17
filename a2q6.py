course_code = int(input("Enter course code (1-7): "))
TIGan = int(input("Is the student from Techno India Group? (1 for Yes, 0 for No): "))
entrance_test = int(input("Has the student qualified the entrance test? (1 for Yes, 0 for No): "))
sex = int(input("Enter gender (1 for Male, 0 for Female): "))

if course_code == 1:
    course_name = "BTech"
    semesters = 8
    admission_fee = 100000
    sem_fee = 75000
elif course_code == 2:
    course_name = "BCA"
    semesters = 6
    admission_fee = 70000
    sem_fee = 50000
elif course_code == 3:
    course_name = "BBA"
    semesters = 6
    admission_fee = 70000
    sem_fee = 50000
elif course_code == 4:
    course_name = "BHHA"
    semesters = 6
    admission_fee = 60000
    sem_fee = 45000
elif course_code == 5:
    course_name = "BSc"
    semesters = 6
    admission_fee = 50000
    sem_fee = 30000
elif course_code == 6:
    course_name = "MBA"
    semesters = 4
    admission_fee = 140000
    sem_fee = 100000
elif course_code == 7:
    course_name = "MCA"
    semesters = 4
    admission_fee = 120000
    sem_fee = 80000
else:
    print("Invalid course code!")
    exit()

# Determine course level
if course_code <= 5:
    level = "UG"
else:
    level = "PG"

# Calculate total fees
if TIGan == 1:
    if level == "UG":
        per_sem_discount = 10000
    else:
        per_sem_discount = 15000

    total_fee = (admission_fee - per_sem_discount) + (semesters - 1) * (sem_fee - per_sem_discount)

else:
    total_fee = admission_fee + (semesters - 1) * sem_fee

    # Entrance scholarship
    if entrance_test == 1:
        total_fee -= 1500

    # Female scholarship
    if sex == 0:
        total_fee -= 10000

# Output result
print("Course Name:", course_name)
print("Total Payable Course Fee: ₹", format(total_fee, ",.2f"))
