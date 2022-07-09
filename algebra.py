def solve_x_on_both_sides(x_side_1: int, x_side_2: int, num_side_1: int, num_side_2: int):
    x_left = x_side_1 - x_side_2
    num_left = num_side_2 - num_side_1
    answer = num_left / x_left
    return answer


def create_linear_sequence(n_num: int, other_num: int):
    sequence = []
    for i in range(1, 6):
        sequence_term = i * n_num + other_num
        sequence.append(str(sequence_term))
    joined_sequence = ", ".join(sequence)
    return joined_sequence


def is_num_in_linear_sequence(num: int, n_num: int, other_num: int):
    inverse_num = other_num * -1
    new_num = num + inverse_num
    new_num_2 = new_num / n_num
    if new_num_2 % 1 == 0:
        return "Yes"
    else:
        return "No"


def num_term_in_linear_sequence(num_term: int, n_num: int, other_num: int):
    term_value = num_term * n_num + other_num
    return term_value


def recurring_decimal_to_fraction(decimal: int):
    num_after_decimal = len(str(decimal).split(".")[1])
    print(num_after_decimal)
    decimal = decimal * pow(10, num_after_decimal)
    return str(int(decimal)) + "/" + num_after_decimal * "9"
