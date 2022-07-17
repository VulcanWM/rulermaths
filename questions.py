import random
import maths
import lists


def side_from_angle_side_question():
    question_type = random.randint(1, 6)
    question_type = str(question_type)
    sides = ["opp", "adj", "hyp"]
    random.shuffle(sides)
    side_find = sides[0]
    side_given = sides[1]
    angle = random.randint(25, 70)
    side_given_length = random.randint(5, 15)
    if question_type == "1":
        side_names = {"hyp": "BC", "opp": "AC", "adj": "AB"}
        right_angle = "<CAB"
        angle_given = "<ABC"
    elif question_type == "2":
        side_names = {"hyp": "BC", "opp": "AB", "adj": "AC"}
        right_angle = "<CAB"
        angle_given = "<ACB"
    elif question_type == "3":
        side_names = {"hyp": "AC", "opp": "AB", "adj": "BC"}
        right_angle = "<CBA"
        angle_given = "<BCA"
    elif question_type == "4":
        side_names = {"hyp": "AC", "opp": "BC", "adj": "AB"}
        right_angle = "<CBA"
        angle_given = "<BAC"
    elif question_type == "5":
        side_names = {"hyp": "AB", "opp": "AC", "adj": "BC"}
        right_angle = "<ACB"
        angle_given = "<ABC"
    else:
        side_names = {"hyp": "AB", "opp": "BC", "adj": "AC"}
        right_angle = "<ACB"
        angle_given = "<CAB"
    question = f"ABC is a right-angled triangle, where {right_angle} is a right angle. " \
               f"If {side_names[side_given]} is {str(side_given_length)} and {angle_given} is {str(angle)}˚" \
               f", what is the length of {side_names[side_find]} to 2 decimal places?"
    trig_map = {
        ('hyp', 'opp'): maths.get_hyp_from_angle_opp,
        ('hyp', 'adj'): maths.get_hyp_from_angle_adj,
        ('adj', 'opp'): maths.get_adj_from_angle_opp,
        ('adj', 'hyp'): maths.get_adj_from_angle_hyp,
        ('opp', 'adj'): maths.get_opp_from_angle_adj,
        ('opp', 'hyp'): maths.get_opp_from_angle_hyp,
    }

    func = trig_map.get((side_find, side_given))
    answer = func(angle, side_given_length)
    return question, answer


def x_on_both_sides_question():
    x_side_1 = random.randint(2, 10)
    x_side_2 = random.randint(2, 10)
    while x_side_2 == x_side_1:
        x_side_2 = random.randint(2, 10)
    num_side_1 = random.randint(2, 10)
    num_side_2 = random.randint(2, 10)
    while num_side_2 == num_side_1:
        num_side_2 = random.randint(2, 10)
    answer = maths.solve_x_on_both_sides(x_side_1, x_side_2, num_side_1, num_side_2)
    sign_1 = "+"
    sign_2 = "+"
    if num_side_1 < 0:
        sign_1 = "-"
        num_side_1 = num_side_1 * -1
    if num_side_2 < 0:
        sign_2 = "-"
        num_side_2 = num_side_2 * -1
    question = f"Solve for x (to 2 decimal places):" \
               f"\n{str(x_side_1)}x {sign_1} {str(num_side_1)} = {str(x_side_2)}x {sign_2} {str(num_side_2)}"
    return question, answer


def linear_sequence_question(question_type=1):
    question_type = str(question_type)
    if question_type == "1" or question_type == "3":
        n_num = random.randint(-9, 9)
        while n_num == 0:
            n_num = random.randint(-9, 9)
    else:
        n_num = random.randint(2, 9)
        while n_num == 0:
            n_num = random.randint(2, 9)
    other_num = random.randint(-9, 9)
    while other_num == 0:
        other_num = random.randint(-9, 9)
    if question_type == "1":
        sequence = maths.create_linear_sequence(n_num=n_num, other_num=other_num)
        question = f"Find the nth term of this sequence: {sequence}"
        sign = "+"
        if other_num < 0:
            sign = "-"
            other_num = other_num * -1
        answer = f"{str(n_num)}n {sign} {str(other_num)}"
    elif question_type == "2":
        num = random.randint(20, 90)
        answer = maths.is_num_in_linear_sequence(num=num, n_num=n_num, other_num=other_num)
        sign = "+"
        if other_num < 0:
            sign = "-"
            other_num = other_num * -1
        question = f"Is {str(num)} in the sequence: {str(n_num)}n {sign} {str(other_num)}?"
    else:
        num_term = random.randint(10, 30)
        if num_term % 10 == 1:
            end = "st"
        elif num_term % 10 == 2:
            end = "nd"
        elif num_term % 10 == 3:
            end = "rd"
        else:
            end = "th"
        answer = maths.num_term_in_linear_sequence(num_term=num_term, n_num=n_num, other_num=other_num)
        sign = "+"
        if other_num < 0:
            sign = "-"
            other_num = other_num * -1
        question = f"What is the {str(num_term)}{end} number in the sequence: {str(n_num)}n {sign} {str(other_num)}?"
    return question, answer


def recurring_decimal_to_fraction_question(question_type=1):
    question_type = str(question_type)
    if question_type == "1":
        decimal = random.randint(2, 9)
        decimal = decimal / 10
        question = f"Convert {str(decimal)} recurring to a fraction."
        answer = maths.recurring_decimal_to_fraction(decimal)
    else:
        decimal = random.randint(20, 90)
        while decimal % 10 == 0:
            decimal = random.randint(20, 90)
        decimal = decimal / 100
        question = f"Convert {str(decimal)} recurring to a fraction."
        answer = maths.recurring_decimal_to_fraction(decimal)
    return question, answer


def is_prime_question():
    number = random.randint(10, 99)
    if number in maths.primes:
        answer = "Yes"
    else:
        answer = "No"
    question = f"Is {str(number)} a prime number?"
    return question, answer


def prime_factorisation_question():
    number = random.randint(10, 100)
    while number in maths.primes:
        number = random.randint(10, 100)
    answer_dict = maths.prime_factorise(number)
    answer_list = []
    for num in list(answer_dict.keys()):
        answer_list.append(f"{num}^{str(answer_dict[num])}")
    answer = "x".join(answer_list)
    question = f"Write the prime factorisation of {str(number)}." \
               f" Use indices always using ^ and order the factors from least to greatest." \
               f"(for example, 3^3x2^1)"
    return question, answer


def lowest_common_multiple_questions():
    question_number = random.randint(1, 3)
    number1 = random.randint(3, 11)
    number2 = random.randint(3, 11)
    while number2 == number1:
        number2 = random.randint(3, 11)
    colour1 = random.choice(lists.colours)
    colour2 = random.choice(lists.colours)
    while colour2 == colour1:
        colour2 = random.choice(lists.colours)
    name = random.choice(lists.names)
    if question_number == 1:
        question = f"{name} is arranging {colour1} blocks in groups of {str(number1)}" \
                   f" and {colour2} blocks in groups of {str(number2)}. " \
                   f"If they have the same number of {colour1} and {colour2} blocks, " \
                   f"what is the smallest number of each colour that {name} could have?"
    elif question_number == 2:
        family_member = random.choice(lists.family_members)
        question = f"{name} notices that his house number is divisible by {str(number1)}, " \
                   f"and their {family_member} notices it is divisible by {str(number2)}. " \
                   f"What is the smallest possible house number?"
    else:
        stationary1 = random.choice(lists.stationary)
        stationary2 = random.choice(lists.stationary)
        while stationary2 == stationary1:
            stationary2 = random.choice(lists.stationary)
        question = f"{name} is buying {stationary1} and {stationary2} from the store. " \
                   f"{stationary1.capitalize()} come in packages of {str(number1)}, " \
                   f"but {stationary2} are sold in packages of {str(number2)}. " \
                   f"If {name} wishes to purchase the same number of {stationary1} as {stationary2}, " \
                   f"what is the smallest number of {stationary2} that they can buy?"
    answer = maths.lowest_common_multiple_2(number1, number2)
    return question, answer


def highest_common_factor_question():
    question_number = random.randint(1, 3)
    main_number = random.randint(3, 11)
    number1 = random.randint(2, 7)
    number2 = random.randint(3, 7)
    while number2 == number1:
        number2 = random.randint(3, 7)
    number1 = main_number * number1
    number2 = main_number * number2
    name = random.choice(lists.names)
    if question_number == 1:
        question = f"{name} has {str(number1)} tulips and {str(number2)} carnations. " \
                   "If they want to create identical bouquets without any leftover flowers" \
                   f", what is the greatest number of bouquets {name} can make?"
    elif question_number == 2:
        subject1 = random.choice(lists.subjects)
        subject2 = random.choice(lists.subjects)
        while subject2 == subject1:
            subject2 = random.choice(lists.subjects)
        question = f"{name} has {str(number1)} {subject1} books and {str(number2)} {subject2} books. " \
                   "If they want to distribute them evenly among some " \
                   "bookshelves so that each bookshelf has the same combination of " \
                   f"{subject1} and {subject2} books, with no books left over, " \
                   f"what is the greatest number of bookshelves {name} can use?"
    else:
        unit = random.choice(lists.units)
        question = f"{name} has two pieces of string, " \
                   f"one {str(number1)} {unit} long and the other {str(number2)} {unit} long. " \
                   f"For a craft project, they want to cut them up to " \
                   f"produce many pieces of string that are all of the same length" \
                   f", with no string left over. What is the greatest length, in {unit}, that she can make them?"
    answer = maths.highest_common_factor_2(number1, number2)
    return question, answer


def classify_numbers_question():
    number_types = ["natural", "integer", "whole", "real", "rational", "irrational"]
    answer_type = random.choice(number_types)
    answers = []
    numbers = []
    number1 = random.randint(2, 15)
    while number1 == 4 or number1 == 9:
        number1 = random.randint(2, 15)
    numbers.append(f"√{str(number1)}")
    if answer_type == "irrational" or answer_type == "real":
        answers.append(f"√{str(number1)}")
    number2 = random.randint(101, 999)
    while number2 % 100 == 0:
        number2 = random.randint(101, 999)
    numbers.append(str(number2))
    if answer_type == "real" or answer_type == "rational":
        answers.append(str(number2))
    # add 0, a number bigger than 0, a number less than 0, a fraction that doesn't simplify to 1
    question = f"Which of these numbers are {answer_type}: {', '.join(numbers)}\n" \
               f"Separate your answer by a comma only (no space) and " \
               f"type in your answers in the order in the list of numbers given."
    return question, ",".join(answers)


print(classify_numbers_question())
