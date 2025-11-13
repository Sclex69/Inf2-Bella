# Check temperature
temperature = 30
if temperature > 25:
    print("It's warm outside!")
else:
    print("It's cool.")

# Check if a number is positive, negative, or zero
number = int(input("write a number"))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

# Check if two numbers are even or odd
number = int(input("write a number"))
number2 = int(input("write a number"))

def check(x):
    # Return 1 if even, 0 if odd
    if x % 2 == 0:
        return 1
    else:
        return 0

number = check(number)
number2 = check(number2)

# Compare parity of both numbers
if number == 1:
    if number2 == 1:
        print("Both even")
    else:
        print("One even, one odd")
else:
    if number2 == 1:
        print("One even, one odd")
    else:
        print("Both odd")

# Password validation
password = input("enter password")
has_permission = True if "python" in password else False

if len(password) > 7 and has_permission:
    print("good password")
else:
    print("bad password")

# Traffic light color check
color = input("color")
if color == "red":
    print("stop")
if color == "green":
    print("Go")
if color == "yellow":
    print("slow down")
else:
    print("invalid color")

# Entry permission based on age and ticket
age = int(input("enter age"))
ticket = input("do you have a ticket?").lower()
has_permission = True if ticket == "yes" else False

if age > 11 and has_permission:
    print("You may enter")
else:
    print("entry denied")

# Compare two numbers using nested if
x = 5
y = 7
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

# Same comparison using chained conditional
x = 5
y = 7
if x == y:
    print('x and y are equal')
elif x < y:
    print('x is less than y')
else:
    print('x is greater than y')

# Check if x is a positive single-digit number
if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

# Single conditional version
if 0 < x < 10:
    print('x is a positive single-digit number.')

# Using not operators (less readable)
if not x <= 0 and not x >= 10:
    print('x is a positive single-digit number.')

# Simplified version
if 0 < x < 10:
    print('x is a positive single-digit number.')

# Check if three sides can form a triangle
def is_triangle(x, y, z):
    # Check largest side against sum of other two sides
    if x < y and z < y:
        if x + z < y:
            return "no"
        else:
            return "yes"
    if y < x and z < x:
        if z + y < x:
            return "no"
        else:
            return "yes"
    if y < z and x < z:
        if x + y < z:
            return "no"
        else:
            return "yes"

# Test triangle function
print(is_triangle(4, 5, 6))   # yes
print(is_triangle(1, 2, 3))   # yes
print(is_triangle(6, 2, 3))   # no
print(is_triangle(1, 1, 12))  # no
