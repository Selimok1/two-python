import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

def is_positive(number):
    if number > 0:
        return True
    else:
        return False
r = 5
print(f"Площадь круга с радиусом {r}: {calculate_circle_area(r):.2f}")

num = -3
print(f"Число {num} положительное? {is_positive(num)}")