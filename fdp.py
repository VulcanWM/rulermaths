def recurring_decimal_to_fraction(decimal: float):
    num_after_decimal = len(str(decimal).split(".")[1])
    decimal = decimal * pow(10, num_after_decimal)
    return str(int(decimal)) + "/" + num_after_decimal * "9"
