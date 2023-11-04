#The name of the pets
pets = [
    {"kind": "Dog", "owner": "Alice"},
    {"kind": "Cat", "owner": "Bob"},
    {"kind": "Parrot", "owner": "Charlie"},
    {"kind": "Fish", "owner": "David"},
    {"kind": "Hamster", "owner": "Eve"}
]
#We print the code
for pet in pets:
    print(f"Kind: {pet['kind']}\nOwner: {pet['owner']}\n")
