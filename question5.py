#Simple Age Checker for minor or adult or senior
age = int(input("Enter your age: "))
if age < 1 or age > 100:
    print("Invalid age entered")
elif age < 18 and age > 0:
    print("You are a minor")
elif age >= 18 and age <= 65:
    print("You are an adult")
elif age > 65 and age <= 100:
    print("You are a senior")
