number_input = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(number_input):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

p1_percent = p1 / number_input * 100
p2_percent = p2 / number_input * 100
p3_percent = p3 / number_input * 100
p4_percent = p4 / number_input * 100
p5_percent = p5 / number_input * 100

print(f"{p1_percent:.02f}%")
print(f"{p2_percent:.02f}%")
print(f"{p3_percent:.02f}%")
print(f"{p4_percent:.02f}%")
print(f"{p5_percent:.02f}%")