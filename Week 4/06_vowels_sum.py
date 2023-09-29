text = input()
value = 0

for letters in text:
    if letters == "a":
        value += 1
    elif letters == "e":
        value += 2
    elif letters == "i":
        value += 3
    elif letters == "o":
        value += 4
    elif letters == "u":
        value += 5

print(value)
