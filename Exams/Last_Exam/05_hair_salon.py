number = int(input())
price = 0

while price < number:
    service = input()

    if service == "closed":
        break

    if service == "haircut":
        service_type = input()
        if service_type == "mens":
            price += 15
        elif service_type == "ladies":
            price += 20
        elif service_type == "kids":
            price += 10
    elif service == "color":
        color_type = input()
        if color_type == "touch up":
            price += 20
        elif color_type == "full color":
            price += 30
    break
difference = abs(number - price)

if price >= number:
    print("You have reached your target for the day!")
    print(f"Earned money: {price}lv.")
else:
    print(f"Target not reached! You need {difference}lv. more.")
    print(f"Earned money: {price}lv.")