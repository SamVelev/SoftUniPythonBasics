days = input()
type_of_room = input()
review = input()
accurate_days = int(days) - 1
price = 0

if type_of_room == "room for one person":
    price = 18
    price *= accurate_days
elif type_of_room == "apartment":
    price = 25
    price *= accurate_days
    if accurate_days < 10:
        price *= 0.7
    elif accurate_days <= 15:
        price *= 0.65
    elif accurate_days > 16:
        price *= 0.5
elif type_of_room == "president apartment":
    price = 35
    price *= accurate_days
    if accurate_days < 10:
        price *= 0.9
    elif accurate_days <= 15:
        price *= 0.85
    elif accurate_days > 16:
        price *= 0.8

if review == "positive":
    price *= 1.25
elif review == "negative":
    price *= 0.9

print(f"{price:.02f}")