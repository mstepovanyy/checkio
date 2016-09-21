def checkio(data):
    
    min_w = 999
    for item in data:
        first = [item,]
        second = data[:]
        second.remove(item)
        tmp = min_weight(first, second)
        if min_w > tmp:
            min_w = tmp
    
    return min_w

def min_weight(first, second):
    min_w = abs(sum(first) - sum(second))
    for item in second:
        new_s = second[:]
        new_s.remove(item)
        new_f = first[:]
        new_f.append(item)
        tmp = min_weight(new_f, new_s)
        if min_w > tmp:
            min_w = tmp
    return min_w


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
