# program that takes a score (0-100) as input and assigns a grade
while True:
    score = int(input("Enter the score to assign grade: "))

    if score >= 90:
        print(f'Grade A')
    elif score >= 80 and score <= 89:
        print("Grade b")
    elif score >= 70 and score <= 79:
        print("Grade c")
    elif score >= 60 and score <= 69:
        print('Grade D')
    elif score >= 100 and score <= 0:
        print("Invalid score entered")
    else:
        print('Grade F')
