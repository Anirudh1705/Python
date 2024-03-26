import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return x ** y

def root(x, y):
    return x ** (1/y)

def natural_log(x):
    return math.log(x)

def base10_log(x):
    return math.log10(x)

def calculate(expression):
    try:
        result = eval(expression)
    except Exception as e:
        return str(e)
    return str(result)

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Root")
    print("7. Natural logarithm (ln)")
    print("8. Base-10 logarithm (log10)")
    print("9. Advanced calculation")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3/4/5/6/7/8/9): "))
        except ValueError:
            print("Invalid input! Please enter 1, 2, 3, 4, 5, 6, 7, 8, or 9.")
            continue

        if choice in (1, 2, 3, 4):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == 2:
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == 3:
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == 4:
                print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == 5:
            num1 = float(input("Enter base number: "))
            num2 = float(input("Enter exponent: "))
            print(num1, "^", num2, "=", exponent(num1, num2))
        elif choice == 6:
            num1 = float(input("Enter the number: "))
            num2 = float(input("Enter the root: "))
            print(num1, "root", num2, "=", root(num1, num2))
        elif choice == 7:
            num1 = float(input("Enter the number: "))
            print("ln(", num1, ") =", natural_log(num1))
        elif choice == 8:
            num1 = float(input("Enter the number: "))
            print("log10(", num1, ") =", base10_log(num1))
        elif choice == 9:
            calculation = input("Enter your calculation with parentheses and operators: ")
            print("Result: ", calculate(calculation))
            break
        else:
            print("Invalid input! Please enter 1, 2, 3, 4, 5, 6, 7, 8, or 9.")

if __name__ == "__main__":
    main()