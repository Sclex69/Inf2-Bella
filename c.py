def pascal_triangle(n):
    triangle = []
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            row = [1]
            for j in range(len(triangle[-1]) - 1):
                row.append(triangle[-1][j] + triangle[-1][j+1])
            row.append(1)
        triangle.append(row)
    return triangle


def save_pascal_to_file(n, filename="pascal.txt"):
    triangle = pascal_triangle(n)
    with open(filename, "w") as f:
        for row in triangle:
            f.write(" ".join(map(str, row)) + "\n")
save_pascal_to_file(8)