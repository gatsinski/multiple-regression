from utils import solve_system, get_answers, get_variables


z = [31.4, 14.6, 6.4, 28.3, 42.1, 15.3]
w = [345, 168, 94, 187, 621, 255]
x = [65, 18, 0, 185, 87, 0]
y = [23, 18, 0, 98, 10, 0]

variables = get_variables(w, x, y, z)
answers = get_answers(w, x, y, z)

solution = solve_system(variables, answers)

print(solution)
