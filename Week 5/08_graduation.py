name_of_student = input()
grades_counter = 0
years_counter = 0
failed_years = 0

while years_counter < 12:
    current_number = float(input())

    if current_number < 4:
        failed_years += 1
        if failed_years > 1:
            excluded_years = years_counter + 1
            print(f"{name_of_student} has been excluded at {excluded_years} grade")
            break

        continue

    grades_counter += current_number
    years_counter += 1

else:
    average_grade = grades_counter / years_counter
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")