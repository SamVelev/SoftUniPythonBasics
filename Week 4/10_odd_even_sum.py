number = int(input())
even_number = 0
odd_number = 0

for even in range(number):
    current_num = int(input())
    if even % 2 == 0:
        even_number += current_num
    else:
        odd_number += current_num

difference = abs(even_number - odd_number)

if even_number == odd_number:
    print("Yes")
    print(f"Sum = {even_number}")
else:
    print("No")
    print(f"Diff = {difference}")


