def checkio(lines_list):
    """Return the quantity of squares"""
    squeres = range(1,4)
    found = 0
    lines_list = [sorted(item) for item in lines_list]
    for sq in squeres:
        for row in range(0, 4 - sq):
            for col in range(0, 4 - sq):
                point = row, col
                if is_squere(lines_list, point, sq):
                    found += 1
    return found

def is_squere(lines, point, width):
    l_number = point[0] * 4 + point[1] + 1
    r_number = point[0] * 4 + point[1] + width + 1
    d_number = point[0] * 4 + width * 4 + point[1] + 1
    x_number = point[0] * 4 + width * 4 + point[1] + width + 1
    if is_line(lines, l_number, r_number, width) and is_line(lines, r_number, x_number, width) and is_line(lines, l_number, d_number, width) and is_line(lines, d_number, x_number, width):
        return True

def is_line(lines, n_1, n_2, width):
    inc = 1 if (n_2 - n_1) == width else 4
    for step in range(n_1, n_2, inc):
        point = [step, step + inc]
        if point not in lines:
            return False
    return True
    
if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"