import copy
def capture(matrix):
    first = 0
    infected = [0]
    crack = {connected:matrix[connected][connected] for connected in get_connected(matrix, 0)}
    for minute in range(1, 999):
        for item, ttl in copy.copy(crack).items():
            crack[item] -= 1
            if crack[item] == 0:
                infected.append(item)
                del crack[item]
                new_connected = get_connected(matrix, item)
                for connection in new_connected:
                    if connection in infected or connection in crack.keys():
                        continue
                    else:
                        crack[connection] = matrix[connection][connection]
        if len(infected) == len(matrix) or not crack:
            return minute
    return 0

def get_connected(matrix, point):
    return [id for id, item in enumerate(matrix[point]) if item == 1 and id != point]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
