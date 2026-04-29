import tkinter as tk
import math

# Settings
SIZE = 400
STEP = 50  # Distance between lines
points = []


def calculate_distances(p1, p2):
    # Standard formulas using grid units (0, 1, 2...)
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    euc = math.sqrt(dx ** 2 + dy ** 2)
    man = abs(dx) + abs(dy)
    return euc, man


def handle_click(event):
    global points

    # SNAP LOGIC:
    # Round the click position to the nearest intersection
    grid_x = round(event.x / STEP)
    grid_y = round(event.y / STEP)

    # Store the point
    points.append((grid_x, grid_y))

    # Draw a small blue dot at the intersection
    pixel_x = grid_x * STEP
    pixel_y = grid_y * STEP
    canvas.create_oval(pixel_x - 4, pixel_y - 4, pixel_x + 4, pixel_y + 4, fill="blue")

    if len(points) == 2:
        euc, man = calculate_distances(points[0], points[1])

        # Draw a line between the two points to show the Euclidean path
        x1, y1 = points[0][0] * STEP, points[0][1] * STEP
        x2, y2 = points[1][0] * STEP, points[1][1] * STEP
        canvas.create_line(x1, y1, x2, y2, fill="red")

        label.config(text=f"Euclidean: {round(euc, 2)} units\nManhattan: {man} units")
        points = []  # Reset for next pair


# --- GUI Setup ---
root = tk.Tk()
root.title("Intersection Snapping")

canvas = tk.Canvas(root, width=SIZE, height=SIZE, bg="white")
canvas.pack()

label = tk.Label(root, text="Click near intersections", font=("Arial", 12))
label.pack(pady=10)

# Draw the Grid Lines
for i in range(0, SIZE + STEP, STEP):
    canvas.create_line(i, 0, i, SIZE, fill="lightgray")  # Vertical
    canvas.create_line(0, i, SIZE, i, fill="lightgray")  # Horizontal

canvas.bind("<Button-1>", handle_click)
root.mainloop()