from os import replace

f = open("f7.txt")
f=f.read()


def count_underpopulated(text):
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

    total = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '@':
                if neighbor_count(x, y) < 4:
                    total += 1

    return total
print(count_underpopulated(f))