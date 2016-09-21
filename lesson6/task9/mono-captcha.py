FONT = ("-XX---X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-",
        "-X-X-XX----X---X-X-X-X---X-----X-X-X-X-X-",
        "-X-X--X---XX--X--XXX-XX--XXX--X--XXX-XXX-",
        "-X-X--X--X-----X---X---X-X-X-X---X-X---X-",
        "--XX--X--XXX-XXX---X-XX---XX-X---XXX-XX--")


def checkio(image):
    #print(split(image))
    #global FONT
    all_map = dict()
    for key, value in enumerate(split(FONT)):
        all_map[key] = value

    # match with original.
    res = ''
    for item in split(image):
        res += match(item, all_map)

    return int(res)

def match(item, original):
    result = dict()
    for digit, number in original.items():
        errors = 0
        for r_id, row in enumerate(number):
            for c_id, c in enumerate(row):
                c = 0 if c == '-' else 1
                if c != item[r_id][c_id]:
                    errors += 1
        result[digit] = errors
    num,_ = min(result.items(), key=lambda x: x[1])
    return str(num)


def split(image):
    #split by number

    split_img = []
    for digit in range(len(image[0])//4):
        split_img.append([[0, 0, 0, 0] for item in range(len(image))]) 

    for r_id, row in enumerate(image):
        for id, value in enumerate(row):
            index = id // 4
            try:
                split_img[index][r_id][id % 4] = value
            except IndexError: pass
    return split_img

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"
