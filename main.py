import questions
import random

question_type = random.randint(1, 6)
print(questions.side_from_angle_side_question(question_type=question_type))

print(questions.x_on_both_sides_question())