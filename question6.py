#Password Validator

password = str(input("Enter password: "))

if password != "python123":
    print("Access denied")
elif password == "python123":
    print("Access granted")