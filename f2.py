count_zero = 0
pos = 50  # starting position

with open("file.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]     # 'L' or 'R'
        steps = int(line[1:])   # whole number of clicks

        # find first click (k in 1..steps) that makes dial 0
        if direction == "R":
            first = (100 - pos) % 100
        else:  # "L"
            first = pos % 100

        # treat 0 as 100 (meaning you would need 100 clicks to hit 0 again)
        if first == 0:
            first = 100

        # if the first occurrence is within the steps, count it and any full 100-click loops after it
        if first <= steps:
            count_zero += 1 + (steps - first) // 100

        # update final position after the rotation
        if direction == "R":
            pos = (pos + steps) % 100
        else:
            pos = (pos - steps) % 100

print(count_zero)
