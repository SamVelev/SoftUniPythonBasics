days = int(input())
type_of_accommodation = input()
review = input()
real_days = days - 1
price_per_night = 0

if type_of_accommodation == "room for one person":
    price_per_night = 18
elif type_of_accommodation == "apartment":
    price_per_night = 25
    if real_days < 10:
        price_per_night *= 0.7
    elif real_days <= 15:
        price_per_night *= 0.65
    elif real_days > 15:
        price_per_night *= 0.5
elif type_of_accommodation == "president apartment":
    price_per_night = 35
    if real_days < 10:
        price_per_night *= 0.9
    elif real_days <= 15:
        price_per_night *= 0.85
    elif real_days > 15:
        price_per_night *= 0.8

total_sum = price_per_night * real_days

if review == "positive":
    total_sum *= 1.25
elif review == "negative":
    total_sum *= 0.9

print(f"{total_sum:.02f}")