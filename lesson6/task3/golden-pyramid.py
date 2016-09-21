def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    ways_count = 2**(len(pyramid) -1)
    binary_format = '{0:0'+ str(len(pyramid))+'b}'
    way_list = []
    max_value = 0
    for way in range(0, ways_count):
        one_way = []
        prev = 0
        for item in binary_format.format(way):
            if item == '1':
                prev += 1
            one_way.append(prev)
        way_list.append(one_way)
    
    for way in way_list:
        current_value = 0
        for row, index in zip(pyramid, way):
            current_value +=  row[index]
        
        if current_value > max_value:
            max_value = current_value

    return max_value


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
