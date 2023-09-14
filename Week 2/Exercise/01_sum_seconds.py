from math import floor

number = int(input())
number_second = int(input())
number_third = int(input())
total_time = number + number_second + number_third
minutes = total_time // 60
seconds = total_time % 60
minutes = floor(minutes)

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")