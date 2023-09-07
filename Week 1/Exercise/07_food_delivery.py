number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegetarian_menus = int(input())
price_for_chicken_menus = number_chicken_menus * 10.35
price_for_fish_menus = number_fish_menus * 12.40
price_for_vegetarian_menus = number_vegetarian_menus * 8.15
total_sum_of_all_menus = price_for_chicken_menus + price_for_fish_menus + price_for_vegetarian_menus
price_for_desert = 0.2 * total_sum_of_all_menus
price_for_delivery = 2.50
total_sum_of_the_order = total_sum_of_all_menus + price_for_desert + price_for_delivery

print(round(total_sum_of_the_order, 2))