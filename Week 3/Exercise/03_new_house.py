type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
price = 0

if type_of_flowers == "Roses":
    price = 5
    if number_of_flowers > 80:
        price *= 0.9
elif type_of_flowers == "Dahlias":
    price = 3.80
    if number_of_flowers > 90:
        price *= 0.85
elif type_of_flowers == "Tulips":
    price = 2.80
    if number_of_flowers > 80:
        price *= 0.85
elif type_of_flowers == "Narcissus":
    price = 3
    if number_of_flowers < 120:
        price *= 1.15
elif type_of_flowers == "Gladiolus":
    price = 2.50
    if number_of_flowers < 80:
        price *= 1.20

sum_left = price * number_of_flowers
difference = abs(budget - sum_left)

if budget >= sum_left:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {difference:.02f} leva left.")
else:
    print(f"Not enough money, you need {difference:.02f} leva more.")