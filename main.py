import random
from sort_questions import all_questions

all_functions = all_questions['KS3']
random_topic = random.choice(list(all_functions.keys()))
random_func = random.choice(all_functions[random_topic])
print(random_func)

