from os import replace

f = open("f7.txt")
f=f.read()

def remove_until_stable(text):
    grid = [list(line) for line in text.split("\n")]
    height = len(grid)
    width = len(grid[0])

    def neighbor_count(x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if grid[ny][nx] == '@':
                        count += 1
        return count

    total_removed = 0

    while True:
        to_remove = []

        # Check which @ need to be removed in this round
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '@' and neighbor_count(x, y) < 4:
                    to_remove.append((x, y))

        # If nothing to remove, we're stable
        if not to_remove:
            break

        # Remove them
        for x, y in to_remove:
            grid[y][x] = '.'

        total_removed += len(to_remove)

    # Turn grid back into text
    final_text = "\n".join("".join(row) for row in grid)

    return final_text, total_removed

final_grid, removed = remove_until_stable(f)
print(final_grid)
print("Total removed:", removed)