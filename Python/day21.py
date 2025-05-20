# 21. Ask for a number input, print an error when it's not a number using if else

user_input = input("Enter a number: ")

if user_input.isdigit():
    number = int(user_input)
    print(f"{number} is a number")
else:
    raise ValueError ("Not a valid number")