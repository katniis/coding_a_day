# 15. print a defined array, then remove the last item using array pop or equivalent

# pop() method is used to remove and return an element from a list.

lyrics: list[str] = [
    "bayang",
    "magiliw",
    "perlas",
    "ng",
    "silanganan",
    "alab",
    "ng",
    "pugo"
]
print(lyrics)

print("Popped Lyrics:", lyrics.pop())
print("New Lyrics:", lyrics)