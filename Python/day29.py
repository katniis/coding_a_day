# 29. Create a function greatest(x,y,z) that returns which of the 3 given numbers are greater (using > or < signs)

def greatest(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
    
print("Input 3 numbers(to know which one is greatest):")
num1 = float(input("Enter Num1: "))
num2 = float(input("Enter Num2: "))
num3 = float(input("Enter Num3: "))

print(f"The largest number is: {greatest(num1,num2,num3)}")
