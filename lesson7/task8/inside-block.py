
def area(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def intersect_position(x1, x2, x3, x4):
    if (x1 > x2):
        (x1, x2) = (x2, x1)
    if (x3 > x4):
        (x3, x4) = (x4, x3)
    return max(x1, x3) <= max(x2, x4)

def intersect(a, b, c, d):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    x4, y4 = d
    return intersect_position(x1, x2, x3, x4) and intersect_position(y1, y2, y3, y4) and area(a, b, c) * area(a, b, d) <=0 and area(c, d, a) * area(c, d, b) <= 0

def group(iterable):
    for i in range(0, len(iterable), 1):
        val = tuple(iterable[i:i+2])
        if len(val) == 2:
            yield tuple(iterable[i:i+2])
    yield (iterable[-1], iterable[0])

def on_line(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    if not( (x1 <= x3 and x3 <= x2) or (x2 <= x3 and x3 <= x1)  ):
        return False
    if not ( (y1 <= y3 and y3 <= y2) or (y2 <= y3 and y3 <= y1) ):
        return False
    
    return abs((x1- x3)*(y2 - y3) - (y1 - y3)*(x2 - x3)) < 0.1
    

def is_inside(polygon, point):
    count = 0
    for first, second in group(polygon):
        if on_line(first, second, point):
            return True
        if intersect(first, second, point, (4, 40)):
            count += 1
    return count % 2 != 0



if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) == False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) == True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) == False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) == True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) == False, "Eighth"


    