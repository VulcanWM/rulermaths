import random
import trigonometry
import algebra
import fdp
import number


def side_from_angle_side_question(question_type=1):
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
        ('hyp', 'opp'): trigonometry.get_hyp_from_angle_opp,
        ('hyp', 'adj'): trigonometry.get_hyp_from_angle_adj,
        ('adj', 'opp'): trigonometry.get_adj_from_angle_opp,
        ('adj', 'hyp'): trigonometry.get_adj_from_angle_hyp,
        ('opp', 'adj'): trigonometry.get_opp_from_angle_adj,
        ('opp', 'hyp'): trigonometry.get_opp_from_angle_hyp,
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
    answer = algebra.solve_x_on_both_sides(x_side_1, x_side_2, num_side_1, num_side_2)
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
        sequence = number.create_linear_sequence(n_num=n_num, other_num=other_num)
        question = f"Find the nth term of this sequence: {sequence}"
        sign = "+"
        if other_num < 0:
            sign = "-"
            other_num = other_num * -1
        answer = f"{str(n_num)}n {sign} {str(other_num)}"
    elif question_type == "2":
        num = random.randint(20, 90)
        answer = number.is_num_in_linear_sequence(num=num, n_num=n_num, other_num=other_num)
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
        answer = number.num_term_in_linear_sequence(num_term=num_term, n_num=n_num, other_num=other_num)
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
        answer = fdp.recurring_decimal_to_fraction(decimal)
    else:
        decimal = random.randint(20, 90)
        while decimal % 10 == 0:
            decimal = random.randint(20, 90)
        decimal = decimal / 100
        question = f"Convert {str(decimal)} recurring to a fraction."
        answer = fdp.recurring_decimal_to_fraction(decimal)
    return question, answer
