annually_tax_for_basketball_training = int(input())
price_for_basketball_shoes = annually_tax_for_basketball_training * 0.6
price_for_basketball_clothing = price_for_basketball_shoes * 0.8
price_for_basketball_ball = 0.25 * price_for_basketball_clothing
price_for_basketball_accessories = 0.20 * price_for_basketball_ball
total_price_for_equipment = annually_tax_for_basketball_training + price_for_basketball_shoes + price_for_basketball_clothing + \
                            price_for_basketball_ball + price_for_basketball_accessories

print(total_price_for_equipment)

