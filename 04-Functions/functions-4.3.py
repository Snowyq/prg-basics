import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    result = math.sqrt(s * (s - a) * (s - b) * (s - c) )
    return result

print(triangle_area(3, 4, 5))
print(triangle_area(5, 12, 13))
print(triangle_area(7, 24, 25))