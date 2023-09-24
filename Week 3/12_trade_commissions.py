type_of_city = input()
sales = float(input())
price = 0
error_data = False

if type_of_city == "Sofia":
    if 0 <= sales <= 500:
        price = sales * 0.05
    elif 500 <= sales <= 1000:
        price = sales * 0.07
    elif 1000 <= sales <= 10000:
        price = sales * 0.08
    elif sales > 10000:
        price = sales * 0.12
    else:
        error_data = True
elif type_of_city == "Varna":
    if 0 <= sales <= 500:
        price = sales * 0.045
    elif 500 <= sales <= 1000:
        price = sales * 0.075
    elif 1000 <= sales <= 10000:
        price = sales * 0.10
    elif sales > 10000:
        price = sales * 0.13
    else:
        error_data = True
elif type_of_city == "Plovdiv":
    if 0 <= sales <= 500:
        price = sales * 0.055
    elif 500 <= sales <= 1000:
        price = sales * 0.08
    elif 1000 <= sales <= 10000:
        price = sales * 0.12
    elif sales > 10000:
        price = sales * 0.145
    else:
        error_data = True
else:
    error_data = True

if not error_data:
    print(f"{price:.02f}")
else:
    print("error")