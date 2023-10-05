length = int(input())
width = int(input())
total_volume = length * width
number_of_pieces_from_the_cake = True
command = input()

while command != "STOP":
    current_number = int(command)
    total_volume -= current_number
    if total_volume < 0:
        number_of_pieces_from_the_cake = False
        break
    command = input()
if number_of_pieces_from_the_cake:
    print(f"{abs(total_volume)} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_volume)} pieces more.")