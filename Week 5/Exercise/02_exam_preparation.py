max_bad_grades = int(input())
average_grade = 0
total_problems_solved = 0
last_problem_solved = ""
unsatisfied_grades_counter = 0
is_failed = False
current_problem = input()

while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        unsatisfied_grades_counter += 1
        if unsatisfied_grades_counter == max_bad_grades:
            is_failed = True
            break
    average_grade += current_grade
    total_problems_solved += 1
    last_problem_solved = current_problem
    current_problem = input()

if is_failed:
    print(f"You need a break, {unsatisfied_grades_counter} poor grades.")
else:
    average_grade /= total_problems_solved
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {total_problems_solved}")
    print(f"Last problem: {last_problem_solved}")