import random

def roll_dice(n):
    return [random.randint(1, 6) for _ in range(n)]

def analyze_rolls():
    for num in [50, 100, 500]:
        rolls = roll_dice(num)
        frequencies = {i: rolls.count(i) for i in range(1, 7)}

        max_val = max(frequencies, key=frequencies.get)
        min_val = min(frequencies, key=frequencies.get)

        with open("dice_stats.txt", "a") as f:
            f.write(f"Pri počte hodov {num} najfrekventovanejšie číslo bolo {max_val} "
                    f"a najmenej frekventované číslo bolo {min_val}.\n")
