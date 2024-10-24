# Triangle Type Checker
A = float(input("Enter length of side A: "))
B = float(input("Enter length of side B: "))
C = float(input("Enter length of side C: "))


if A == B == C:
    print("Equilateral triangle")
elif A == B or B == C or A == C:
    print('Isosceles triangle')
else:
     print("Scalene triangle")