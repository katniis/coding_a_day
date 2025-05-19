# 17. print out unique characters from a string using built-in array-unique function or it's equivalent

# dict.fromkeys() creates a dictionary using the given iterable as keys.

name = "Peter"
unique_chars = list(dict.fromkeys(name))
print("\n".join(unique_chars))
