number_of_food_packages_for_dogs = int(input())
number_of_food_packages_for_cats = int(input())
food_package_price_for_dogs = number_of_food_packages_for_dogs * 2.50
food_package_price_for_cats = number_of_food_packages_for_cats * 4
final_price = food_package_price_for_dogs + food_package_price_for_cats

print(f"{final_price} lv.")