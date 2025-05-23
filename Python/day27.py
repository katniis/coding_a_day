# 27. Create a function that will subtract y from x, but only until zero

def subtract(x,y):
    return max(x - y, 0)

print("Input 2 number")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

print(f"Subtracted: {subtract(num1, num2)}")