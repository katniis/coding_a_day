# 25. Create function: add(x,y) that returns the sum of 2 numbers

def sum(x,y) -> int:
    return x + y

print("Input 2 number")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

print(f"Sum: {sum(num1, num2)}")