number = int(input())
total_rating = 0
total_sales = 0

for num in range(number):
    current_number = int(input())
    rating = current_number % 10
    sales = current_number // 10

    if rating == 2:
        sales *= 0
    elif rating == 3:
        sales *= 0.5
    elif rating == 4:
        sales *= 0.7
    elif rating == 5:
        sales *= 0.85
    elif rating == 6:
        sales *= 1

    total_rating += rating
    total_sales += sales

average_rating = total_rating / number

print(f"{total_sales:.02f}")
print(f"{average_rating:.02f}")