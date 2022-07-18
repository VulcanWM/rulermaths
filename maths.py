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


def highest_common_factor_2(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    hcf = 1
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


def highest_common_factor_3(x, y, z):
    if x < y and x < z:
        smallest = x
    elif y < z:
        smallest = y
    else:
        smallest = z
    hcf = 1
    for i in range(1, smallest + 1):
        if (x % i == 0) and (y % i == 0) and (z % i == 0):
            hcf = i
    return hcf


def lowest_common_multiple_2(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


def lowest_common_multiple_3(x, y, z):
    largest = 1
    if x > y and x > z:
        largest = x
    if y > x > z:
        largest = y
    if z > x and z > y:
        largest = z
    while True:
        if (largest % x == 0) and (largest % y == 0) and (largest % z == 0):
            lcm = largest
            break
        largest += 1
    return lcm


def is_natural_number(number: int):
    if number > 0 and number % 1 == 0:
        return True
    else:
        return False


def is_integer(number: float):
    if number % 1 == 0:
        return True
    else:
        return False


def is_whole_number(number: float):
    if number > -1 and number % 1 == 0:
        return True
    else:
        return False


def compare_numbers_2(number1: float, number2: float):
    if number1 == number2:
        sign = "="
    elif number1 > number2:
        sign = ">"
    else:
        sign = "<"
    return sign


def compare_numbers_3(fraction_nom: int, fraction_den: int, decimal: float, percentage: float):
    percentage_num = percentage / 100
    fraction = fraction_nom / fraction_den
    numbers = [fraction, decimal, percentage_num]
    sorted_numbers = sorted(numbers)
    real_number_list = []
    for i in range(0,3):
        if sorted_numbers[i] == percentage_num:
            real_number_list.append(f"{str(int(sorted_numbers[i]*100))}%")
        elif sorted_numbers[i] == fraction_nom / fraction_den:
            real_number_list.append(f"{str(fraction_nom)}/{str(fraction_den)}")
        else:
            real_number_list.append(str(sorted_numbers[i]))
    return real_number_list
