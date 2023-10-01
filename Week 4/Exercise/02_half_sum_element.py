import sys

number = int(input())
max_number = -sys.maxsize
sum_numbers = 0
for num in range(number):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number

difference = abs(max_number - (sum_numbers - max_number))

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {difference}")
