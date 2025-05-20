# 26. Create functions: subtract(x,y), divide(x,y), multiply(x,y)

def subtract(x,y):
    return x - y


def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError ("Cannot divide by zero")
    else: 
        return x / y

print("[1] Subtraction\n[2] Multiplication\n[3] Division")
choice = input('Enter Operation: ')

print("Input 2 Integer: ")
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

match choice:   # Python 3.10+
    case "1":
        print(subtract(num1, num2))
    case "2":
        print(multiply(num1, num2))
    case "3":
        print(divide(num1, num2))