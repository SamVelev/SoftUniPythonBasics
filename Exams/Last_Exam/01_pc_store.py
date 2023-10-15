price_for_processor = float(input())
price_for_video_card = float(input())
price_for_ram = float(input())
number_of_rams = int(input())
discount_percentage = float(input())

price_for_processor *= 1.57
price_for_video_card *= 1.57
price_for_ram *= 1.57

total_price_for_ram = price_for_ram * number_of_rams
price_of_processor_after_discount = price_for_processor - (price_for_processor * discount_percentage)
price_for_video_card_after_discount = price_for_video_card - (price_for_video_card * discount_percentage)
total_sum = price_of_processor_after_discount + price_for_video_card_after_discount + total_price_for_ram

print(f"Money needed - {total_sum:.02f} leva.")
