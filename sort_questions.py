import questions

all_questions = {
    "KS2": {
        "Number": [
            questions.linear_sequence_question(1),
            questions.linear_sequence_question(2),
            questions.linear_sequence_question(3),
            questions.is_prime_question(),
            questions.prime_factorisation_question(),
            questions.lowest_common_multiple_questions(),
            questions.highest_common_factor_question(),
            questions.compare_numbers_question()
        ]
    },
    "KS3": {
        "Number": [
            questions.linear_sequence_question(1),
            questions.linear_sequence_question(2),
            questions.linear_sequence_question(3),
            questions.is_prime_question(),
            questions.prime_factorisation_question(),
            questions.lowest_common_multiple_questions(),
            questions.highest_common_factor_question(),
            questions.compare_numbers_question()
        ],
        "Trigonometry": [
            questions.side_from_angle_side_question()
        ],
        "Fractions, Decimals and Percentages": [
            questions.recurring_decimal_to_fraction_question(1),
            questions.recurring_decimal_to_fraction_question(2),
        ],
        "Algebra": [
            questions.x_on_both_sides_question()
        ]
    }
}
