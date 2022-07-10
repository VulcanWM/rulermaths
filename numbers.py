primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


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
