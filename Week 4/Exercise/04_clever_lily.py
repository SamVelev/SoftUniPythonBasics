age_of_lily = int(input())
price_of_washing_machine = float(input())
price_of_toy = int(input())
total_money = 0
total_toys = 0
current_birthday_money = 0

for birthday in range(1, age_of_lily + 1):
    if birthday % 2 == 0:
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else:
        total_toys += 1

total_money += total_toys * price_of_toy
difference = abs(total_money - price_of_washing_machine)

if total_money >= price_of_washing_machine:
    print(f"Yes! {difference:.02f}")
else:
    print(f"No! {difference:.02f}")