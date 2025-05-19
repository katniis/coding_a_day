# 18. Ask for a input, print out the unique characters on that input

user_input = input("Input a string: ")
name_char = list(user_input.upper())
unique_char = dict.fromkeys(name_char)
print("\n".join(unique_char))

