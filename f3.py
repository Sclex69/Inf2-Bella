f="1090286-1131879,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

f = f.split(",")
counter = 0

for i in f:
    start, end = map(int, i.split("-"))
    rozdiel = end - start
    for c in range(rozdiel + 1):
        x = start + c
        s = str(x)

        # --- MINIMAL CHANGE: exact-two-halves test ---
        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            counter += x

print(counter)
