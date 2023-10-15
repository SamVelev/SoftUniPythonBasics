pocket_money_per_day = float(input())
money_earned_per_day = float(input())
total_expenses = float(input())
price_for_present = float(input())

saved_pocket_money = 5 * pocket_money_per_day
earned_money = 5 * money_earned_per_day
total_saved_money = saved_pocket_money + earned_money
total_saved_money_after_expenses = total_saved_money - total_expenses

difference = abs(total_saved_money_after_expenses - price_for_present)

if total_saved_money_after_expenses > price_for_present:
    print(f"Profit: {total_saved_money_after_expenses:.02f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {difference:.02f} BGN.")