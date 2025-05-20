# 23. Ask for a string input for numbers 1 to 10 in words (e.g. one, two...) then output it's translation in tagalog

number_translation = {
    "one": "Isa",
    "two": "Dalawa",
    "three": "Tatlo",
    "four": "Apat",
    "five": "Lima",
    "six": "Anim",
    "seven": "Pito",
    "eight": "Walo",
    "nine": "Siyam",
    "ten": "Sampo"
}

user_input = input("Enter number from 1 to 10: ").lower()
print(f"{user_input} in tagalog is {number_translation[user_input]}")
