# 22. Ask for a number input, throw an error if it's more than 100 or less than zero

try:
    number = int(input("Enter a number from 0 to 100: "))
    if number <= 0 or number >= 100:
        raise ValueError ("Number must be in 0 to 100")
    print(f"You entered {number}")
except ValueError as e:
    print(f"Invalid input {e}")