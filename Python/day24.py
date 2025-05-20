# 24. (formerly day18) print out unique characters and their count on a string

name: str = "Peter Dela Rosa"

char_count = {}

for char in name:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(f"{char}: {count}")