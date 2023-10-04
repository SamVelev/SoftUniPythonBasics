number_of_payments = 0

while True:
    text = input()

    if text == "NoMoreMoney":
        break

    current_number = float(text)

    if current_number >= 0:
        number_of_payments += current_number
        print(f"Increase: {current_number:.02f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {number_of_payments:.02f}")