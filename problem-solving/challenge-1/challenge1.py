def numbers_fraction_calculator(numbers: [int]) -> dict:
    n = len(numbers)
    positive = len(list(filter(lambda x: x > 0, numbers)))
    negative = len(list(filter(lambda x: x < 0, numbers)))
    zero = len(list(filter(lambda x: x == 0, numbers)))
    return {
        "positives": round(positive/n, 6),
        "negative": round(negative/n, 6),
        "zeros": round(zero/n, 6),
    }
