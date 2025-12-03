count_zero = 0
pos = 50   # starts at 50

with open("file.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]       # 'L' or 'R'
        steps = int(line[1:])     # the full number, however many digits

        if direction == "R":
            pos = (pos + steps) % 100
        else:  # direction == "L"
            pos = (pos - steps) % 100

        if pos == 0:
            count_zero += 1

print(count_zero)
