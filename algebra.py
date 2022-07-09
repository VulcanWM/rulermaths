def solve_x_on_both_sides(x_side_1: int, x_side_2: int, num_side_1: int, num_side_2: int):
    x_left = x_side_1 - x_side_2
    num_left = num_side_2 - num_side_1
    answer = num_left / x_left
    return round(answer, 2)

