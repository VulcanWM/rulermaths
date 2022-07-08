import random
import trigonometry


def side_from_angle_side_question(question_type=1):
    sides = ["opp", "adj", "hyp"]
    random.shuffle(sides)
    side_find = sides[0]
    side_given = sides[1]
    angle = random.randint(25, 70)
    side_given_length = random.randint(5, 15)
    if str(question_type) == "1":
        side_names = {"hyp": "BC", "opp": "AC", "adj": "AB"}
        right_angle = "<CAB"
        angle_given = "<ABC"
    elif str(question_type) == "2":
        side_names = {"hyp": "BC", "opp": "AB", "adj": "AC"}
        right_angle = "<CAB"
        angle_given = "<ACB"
    elif str(question_type) == "3":
        side_names = {"hyp": "AC", "opp": "AB", "adj": "BC"}
        right_angle = "<CBA"
        angle_given = "<BCA"
    elif str(question_type) == "4":
        side_names = {"hyp": "AC", "opp": "BC", "adj": "AB"}
        right_angle = "<CBA"
        angle_given = "<BAC"
    elif str(question_type) == "5":
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
