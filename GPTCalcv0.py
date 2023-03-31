def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0: # check for division by zero
        print("Cannot Divide By Zero")
    else:
        return float(x / y)

print("Select operation.")
print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")

while True:
    choice = input("Enter operator (+, -, *, or /): ")

    # Check if choice is one of the four options
    if choice in ('+', '-', '*', '/'):
        num1 = int(input("\nEnter first number: "))
        num2 = int(input("\nEnter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '/':
            result = divide(num1, num2)
            if result is not None:
                print("{:.3f}".format(divide(round(float(num1), 6), round(float(num2), 6))))
        break
    else:
        print("Invalid Input")
