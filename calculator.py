a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("""-------------- Digital Calculator ------------------
Available Operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Percentage
-----------------------------------------------------""")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("The result of addition is =", a + b)

elif choice == 2:
    print("The result of subtraction is =", a - b)

elif choice == 3:
    print("The result of multiplication is =", a * b)

elif choice == 4:
    if b != 0:
        print("The result of division is =", a / b)
    else:
        print("The second number must not be zero.")

elif choice == 5:
    if b != 0:
        print("The result of modulus is =", a % b)
    else:
        print("The second number must not be zero.")

elif choice == 6:
    if b != 0:
       print("The result of percentage is =", (a / b) * 100, "%")
    else:
        print("The second number must not be zero.")

else:
    print("You have entered the wrong choice.")
