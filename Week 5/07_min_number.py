numbers = []

while True:
    current_text = input()

    if current_text == "Stop":
        break
    current_number = int(current_text)
    numbers.append(current_number)

print(min(numbers))