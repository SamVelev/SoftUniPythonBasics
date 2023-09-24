type_of_screening = input()
rows = int(input())
columns = int(input())
price = 0

if type_of_screening == "Premiere":
    price = rows * columns * 12
elif type_of_screening == "Normal":
    price = rows * columns * 7.50
elif type_of_screening == "Discount":
    price = rows * columns * 5

print(f"{price:.02f}")