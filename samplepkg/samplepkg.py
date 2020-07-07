def supercharge(num):
    """
    Supercharges a number by multiplying it with "the answer to life,
    the universe and everything"

    Args:
        num (int): some number
    Returns
        int
    """
    if not isinstance(num, int):
        raise TypeError("Please provide an int argument.")

    ANSWER_TO_ULTIMATE_QUESTION = 42
    
    return num * ANSWER_TO_ULTIMATE_QUESTION
