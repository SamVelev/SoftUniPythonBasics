number = int(input())
total_sum_number = 0

while True:
    current_number = int(input())
    total_sum_number += current_number

    if total_sum_number >= number:
        print(total_sum_number)
        break