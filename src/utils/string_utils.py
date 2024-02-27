def int_to_position(number: int) -> str:
    if number % 100 in [11, 12, 13]:  # handling special cases for 11th, 12th, 13th
        suffix = "th"
    else:
        suffixes = {1: "st", 2: "nd", 3: "rd"}
        suffix = suffixes.get(number % 10, "th")

    return str(number) + suffix
