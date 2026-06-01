import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("\nScientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Sin")
    print("6. Cos")
    print("7. Tan")
    print("8. Degree to Radian")
    print("9. Radian to Degree")
    print("10. Square Root")
    print("11. Power")
    print("12. Pi Value")
    print("13. Exit")

    choice = input("Enter choice: ")

    if choice in ["1", "2", "3", "4", "11"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(a, b))

        elif choice == "2":
            print("Result:", subtract(a, b))

        elif choice == "3":
            print("Result:", multiply(a, b))

        elif choice == "4":
            print("Result:", divide(a, b))

        elif choice == "11":
            print("Result:", math.pow(a, b))

    elif choice in ["5", "6", "7", "8", "9", "10"]:
        value = float(input("Enter value: "))

        if choice == "5":
            print("Result:", math.sin(math.radians(value)))

        elif choice == "6":
            print("Result:", math.cos(math.radians(value)))

        elif choice == "7":
            print("Result:", math.tan(math.radians(value)))

        elif choice == "8":
            print("Result:", math.radians(value))

        elif choice == "9":
            print("Result:", math.degrees(value))

        elif choice == "10":
            print("Result:", math.sqrt(value))

    elif choice == "12":
        print("Pi Value:", math.pi)

    elif choice == "13":
        break
