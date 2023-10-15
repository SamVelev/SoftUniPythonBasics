number = int(input())
first_digit = number // 100
second_digit = (number % 100) // 10
third_digit = number % 10

for third_number in range(1, third_digit + 1):
    for second_number in range(1, second_digit + 1):
        for first_number in range(1, first_digit + 1):
            result = first_number * second_number * third_number
            print(f"{third_number} * {second_number} * {first_number} = {result};")