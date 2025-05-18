# 13. loop through a numeric array printing both the index and the value

# enumerate() is a built-in Python function that adds an automatic counter (index) to an iterable like a list, tuple, or string.

names: str = [
    "John",
    "Clark",
    "Tanggol",
    "Michael",
    "Raull",
    "Sahur",
    "Abby",
    "Marky",
    "Gab",
    "Raide",
    "Byre",
    "Sebby",
    "Jv",
    "Raul",
    "VmosPro547",
    "Zura",
    "Kanor",
    "Kiko",
    "Diwata",
    "Los",
    "Mik",
    "Andy",
    "Umaay",
    "Cayatano",
    "Darry",
    "Imee",
    "Almagro"
]

for i, name in enumerate(names):
    print(f"{i}: {name}")