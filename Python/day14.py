# 14. split a name string into a char-array, then capitalize the first letter by overwriting char-array item zero, then reconstruct into a string

name: str = "John"
name_list: str = list(name)
name_list[0] = name_list[0].upper()
capitalize_name = "".join(name_list)

print(capitalize_name)