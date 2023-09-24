budget = int(input())
season = input()
number_of_fishermen = int(input())
price_per_boat = 0

if season == "Spring":
    price_per_boat = 3000
elif season == "Summer" or season == "Autumn":
    price_per_boat = 4200
elif season == "Winter":
    price_per_boat = 2600

if number_of_fishermen <= 6:
    price_per_boat *= 0.9
elif number_of_fishermen <= 11:
    price_per_boat *= 0.85
elif number_of_fishermen >= 12:
    price_per_boat *= 0.75

if number_of_fishermen % 2 == 0 and season != "Autumn":
    price_per_boat *= 0.95

difference = abs(budget - price_per_boat)

if budget >= price_per_boat:
    print(f"Yes! You have {difference:.02f} leva left.")
else:
    print(f"Not enough money! You need {difference:.02f} leva.")