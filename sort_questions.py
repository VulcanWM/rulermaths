import questions

all_questions = {
    "KS2": {
        "Number": {
            "Linear Sequences": [
                questions.linear_sequence_question(1),
                questions.linear_sequence_question(2),
                questions.linear_sequence_question(3)
            ],
            "Prime Numbers": [
                questions.is_prime_question(),
                questions.prime_factorisation_question()
            ],
            "LCM": [
                questions.lowest_common_multiple_questions()
            ],
            "HCF": [
                questions.highest_common_factor_question()
            ],
            "Compare numbers": [
                questions.compare_numbers_question()
            ]
        }
    },
    "KS3": {
        "Number": {
            "Linear Sequences": [
                questions.linear_sequence_question(1),
                questions.linear_sequence_question(2),
                questions.linear_sequence_question(3)
            ],
            "Prime Numbers": [
                questions.is_prime_question(),
                questions.prime_factorisation_question()
            ],
            "LCM": [
                questions.lowest_common_multiple_questions()
            ],
            "HCF": [
                questions.highest_common_factor_question()
            ],
            "Compare Numbers": [
                questions.compare_numbers_question()
            ]
        },
        "Trigonometry": {
            "Side from Side and Angle": [
                questions.side_from_angle_side_question()
            ]
        },
        "Fractions, Decimals and Percentages": {
            "Recurring Decimals": [
                questions.recurring_decimal_to_fraction_question(1),
                questions.recurring_decimal_to_fraction_question(2)
            ]
        },
        "Algebra": {
            "Solve linear equations": [
                questions.x_on_both_sides_question()
            ]
        }
    }
}
