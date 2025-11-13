import math

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def floor_divide(a, b):
    return a // b
def modulus(a, b):
    return a % b
def power(a, b):
    return a ** b

# Average of two numbers
def avarage(a, b):
    return add(a, b) / 2

# Rectangle calculations
def area_rectangle(length, width):
    return multiply(length, width)

def perimeter_rectangle(length, width):
    return 2 * (length + width)

# Triangle area
def area_triangle(base, height):
    return multiply(base, height) / 2

# Pythagoras theorem: returns hypotenuse
def pythagoras(a, b):
    return math.sqrt(power(a, 2) + power(b, 2))

# Quadratic roots: returns two solutions
def quadratic_roots(a, b, c):
    discriminant = math.sqrt(power(b, 2) - 4 * a * c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2


# Exercise 4.1: Distance between two points
def distance(x1, y1, x2, y2):
    # Distance formula: sqrt((x2-x1)^2 + (y2-y1)^2)
    return math.sqrt(power(x2 - x1, 2) + power(y2 - y1, 2))

# Exercise 4.2: Body Mass Index (BMI)
def bmi(weight, height):
    # BMI formula: weight (kg) / height^2 (m^2)
    return weight / power(height, 2)

# Exercise 4.3: Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    # Fahrenheit formula: F = (C * 9/5) + 32
    return (c * 9/5) + 32

# Easter Sunday calculation
def easter_date(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return month, day

# Factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by current number
    return result

