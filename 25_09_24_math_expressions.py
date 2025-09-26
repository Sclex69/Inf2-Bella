def add(a, b):
    return a + b
print(add(1, 2))

def subtract(a,b):
    return a-b
print(subtract(1,2))

def multiply(a,b):
    return a*b
print(multiply(1,2))

def divide(a,b):
    return a/b
print(divide(1,2))

def floor_divide(a,b):
    return a//b
print(floor_divide(1,2))

def modulus(a,b):
    return a%b
print(modulus(1,2))

def power(a,b):
    return a**b
print(power(1,2))

def avarage(a,b):
    return add(a,b)/2
print(avarage(1,2))

def area_rectangle(lenght,width):
    return multiply(lenght,width)
print(area_rectangle(2,3))

def perimeter_rectangle(lenght,width):
    return 2*(lenght+width)
print(perimeter_rectangle(2,3))

def area_triangle(base, height):
    return multiply(base,height)/2
print(area_triangle(2,3))

def pythagoras(a,b):
    return 0.5**(power(a,2)+power(b,2))
print(pythagoras(2,3))

def quadratic_roots(a,b,c):
    root1=(-b+(0.5**(power(a,2)-4*multiply(a,c))))/2*a
    root2=(-b-(0.5**(power(a,2)-4*multiply(a,c))))/2*a
    return root1,root2
print(quadratic_roots(2,3,4))

def distance(x1,y1,x2,y2):
