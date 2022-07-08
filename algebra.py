def solve_x_on_both_sides(x_side_1, x_side_2, num_side_1, num_side_2):
    x_left = x_side_1 - x_side_2
    num_left = num_side_2 - num_side_1
    answer = num_left / x_left
    return answer
