import random

possibilities = ["heads", "tails"]

def cf():
    """Return a random coin flip result.

    Chooses randomly between "heads" and "tails" using the
    `random.choice` function.

    Returns:
        str: The result of the coin flip, either "heads" or "tails".
    """
    result = random.choice(possibilities)
    return result

print(cf())

