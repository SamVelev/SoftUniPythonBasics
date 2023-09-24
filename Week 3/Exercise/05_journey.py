budget = float(input())
season = input()
location = ""
accommodation = ""
price = 0

if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        price = budget * 0.3
    elif season == "winter":
        accommodation = "Hotel"
        price = budget * 0.7
elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        price = budget * 0.4
    elif season == "winter":
        accommodation = "Hotel"
        price = budget * 0.8
elif budget > 1000:
    location = "Europe"
    accommodation = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {location}")
print(f"{accommodation} - {price:.02f}")