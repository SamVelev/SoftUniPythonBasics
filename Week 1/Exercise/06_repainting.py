necessary_amount_of_nylon = int(input())
necessary_amount_paint = int(input())
amount_diluent = int(input())
total_hours = int(input())
price_of_plastic_bags = 0.40
price_of_nylon = (necessary_amount_of_nylon + 2) * 1.50
price_of_paint = (necessary_amount_paint * 1.10) * 14.50
price_of_diluent = amount_diluent * 5.00
total_sum = price_of_nylon + price_of_paint + price_of_diluent + price_of_plastic_bags
price_for_work = (total_sum * 0.3) * total_hours
final_sum = total_sum + price_for_work

print(final_sum)

