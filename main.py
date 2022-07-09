import questions
import random

question_type = random.randint(1, 6)
print(questions.side_from_angle_side_question(question_type=question_type))

print(questions.x_on_both_sides_question())

question_type = random.randint(1, 3)
print(questions.linear_sequence_question(question_type=question_type))

question_type = random.randint(1, 2)
print(questions.recurring_decimal_to_fraction_question(question_type=question_type))