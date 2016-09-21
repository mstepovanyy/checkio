import math
def checkio(a, b, c):
    if a+b > c and b + c > a and a + c > b:
        c_angle = math.acos((a**2 + b**2 - c**2)/(2*a*b))
        b_angle = math.acos((a**2 + c**2 - b**2)/(2*a*c))
        a_angle = math.acos((b**2 + c**2 - a**2)/(2*b*c))
        return sorted([round(math.degrees(c_angle)), round(math.degrees(b_angle)), round(math.degrees(a_angle))])
    else:
        return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
