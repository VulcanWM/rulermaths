import math
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def solve_x_on_both_sides(x_side_1: int, x_side_2: int, num_side_1: int, num_side_2: int):
    x_left = x_side_1 - x_side_2
    num_left = num_side_2 - num_side_1
    answer = num_left / x_left
    return round(answer, 2)


def recurring_decimal_to_fraction(decimal: float):
    num_after_decimal = len(str(decimal).split(".")[1])
    decimal = decimal * pow(10, num_after_decimal)
    return str(int(decimal)) + "/" + num_after_decimal * "9"


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


def prime_factorise(n):
    prime_factors = {}
    while n % 2 == 0:
        if "2" in list(prime_factors.keys()):
            num_of_2 = prime_factors['2']
            del prime_factors['2']
            prime_factors['2'] = num_of_2 + 1
        else:
            prime_factors['2'] = 1
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if str(int(i)) in list(prime_factors.keys()):
                num_of_i = prime_factors[str(int(i))]
                del prime_factors[str(int(i))]
                prime_factors[str(int(i))] = num_of_i + 1
            else:
                prime_factors[str(int(i))] = 1
            n = n / i
    if n > 2:
        if str(int(n)) in list(prime_factors.keys()):
            num_of_n = prime_factors[str(int(n))]
            del prime_factors[str(int(n))]
            prime_factors[str(int(n))] = num_of_n + 1
        else:
            prime_factors[str(int(n))] = 1
    return prime_factors


def get_angle_from_opp_hyp(o, h, dec=2):
    num = o / h
    radian = math.asin(num)
    degrees = math.degrees(radian)
    return round(degrees, dec)


def get_angle_from_opp_adj(o, a, dec=2):
    num = o / a
    radian = math.atan(num)
    degrees = math.degrees(radian)
    return round(degrees, dec)


def get_angle_from_adj_hyp(a, h, dec=2):
    num = a / h
    radian = math.acos(num)
    degrees = math.degrees(radian)
    return round(degrees, dec)


def get_adj_from_angle_hyp(angle, h, dec=2):
    a = h * math.cos(math.radians(angle))
    return round(a, dec)


def get_hyp_from_angle_adj(angle, a, dec=2):
    h = a / math.cos(math.radians(angle))
    return round(h, dec)


def get_opp_from_angle_hyp(angle, h, dec=2):
    o = h * math.sin(math.radians(angle))
    return round(o, dec)


def get_hyp_from_angle_opp(angle, o, dec=2):
    h = o / math.sin(math.radians(angle))
    return round(h, dec)


def get_adj_from_angle_opp(angle, o, dec=2):
    a = o / math.tan(math.radians(angle))
    return round(a, dec)


def get_opp_from_angle_adj(angle, a, dec=2):
    o = a * math.tan(math.radians(angle))
    return round(o, dec)