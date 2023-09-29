import sys

number = int(input())
lowest_number = sys.maxsize
highest_number = -sys.maxsize

for _ in range(number):
    num = int(input())
    if num < lowest_number:
        lowest_number = num
    if num > highest_number:
        highest_number = num

print(f"Max number: {highest_number}")
print(f"Min number: {lowest_number}")