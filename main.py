import random
import trigonometry

sides = ["opp", "adj", "hyp"]
random.shuffle(sides)
side_find = sides[0]
side_given = sides[1]
angle = random.randint(25, 70)
side_given_length = random.randint(5, 15)
side_names = {"hyp": "BC", "opp": "AC", "adj": "AB"}
question = f"ABC is a right-angled triangle, where <CAB is a right angle. " \
           f"If {side_names[side_given]} is {str(side_given_length)} and <ABC is {str(angle)}˚" \
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
print(question)
print(answer)
