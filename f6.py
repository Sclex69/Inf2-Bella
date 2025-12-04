
K=12
def best_k_digits(s, k=K):
    stack = []
    n = len(s)
    for i, ch in enumerate(s):
        # while last picked is smaller than current and we can still fill k digits later
        while stack and stack[-1] < ch and len(stack) + (n - i) > k:
            stack.pop()
        stack.append(ch)
    # keep only first k digits (stack may be longer)
    result = ''.join(stack)[:k]

    return result

total = 0
with open("c.txt") as fh:
    for line_no, line in enumerate(fh, start=1):
        s = line.strip()
        if not s:
            continue
        best = best_k_digits(s, K)
        total += int(best)

print(total)
