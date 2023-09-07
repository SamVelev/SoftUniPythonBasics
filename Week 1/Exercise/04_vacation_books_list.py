from math import floor
number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
hours_needed_in_total = number_of_pages / pages_per_hour
hours_needed_per_day = hours_needed_in_total / number_of_days

print(floor(hours_needed_per_day))
