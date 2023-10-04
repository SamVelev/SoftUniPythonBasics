sum_needed = float(input())
current_sum = float(input())
total_sum_of_past_days = 0
spend_counter = 0

while current_sum < sum_needed and spend_counter < 5:
    current_text = input()
    money = float(input())
    total_sum_of_past_days += 1
    if current_text == "save":
        current_sum += money
        spend_counter = 0
    elif current_text == "spend":
        current_sum -= money
        spend_counter += 1
        if current_sum < 0:
            current_sum = 0

if spend_counter == 5:
    print("You can't save the money.")
    print(total_sum_of_past_days)
elif current_sum >= sum_needed:
    print(f"You saved the money for {total_sum_of_past_days} days.")