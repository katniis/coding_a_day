# 28. Create a function square(x) that returns the square of the number

def squared(x):
    return x ** 2

num = int(input("Enter a number to square: "))
print(f"Squared: {squared(num)}")