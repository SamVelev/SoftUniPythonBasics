deposit_sum = float(input())
deposit_deadline_in_months = int(input())
annual_interest_rate_percent = float(input())
annual_interest_rate = deposit_sum * annual_interest_rate_percent / 100
monthly_interest = annual_interest_rate / 12
whole_sum = deposit_sum + (deposit_deadline_in_months * monthly_interest)

print(whole_sum)