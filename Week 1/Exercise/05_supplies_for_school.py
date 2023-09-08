number_of_pencil_packages = int(input())
number_of_markers_packages = int(input())
detergent = int(input())
percentage_discount = int(input())
price_of_pencil_packages = number_of_pencil_packages * 5.80
price_of_markers_packages = number_of_markers_packages * 7.20
price_of_detergent = detergent * 1.20
total_sum_of_all_materials = price_of_pencil_packages + price_of_markers_packages + price_of_detergent
price_with_discount = total_sum_of_all_materials - (total_sum_of_all_materials * percentage_discount / 100)

print(round(price_with_discount, 2))
