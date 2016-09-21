def break_rings(rings):
    return break_rings_max(rings) if break_rings_max(rings) < break_rings_min(rings) else break_rings_min(rings)
    
def break_rings_max(rings):
    rings_broken = 0
    while rings:
        item = max_count(frequency_of_rings(rings))
        rings = [ring_connection for ring_connection in rings if item[0] not in ring_connection]
        rings_broken += 1
    return rings_broken

def break_rings_min(rings):
    total_rings = len(rings)
    save_rings = []
    rings_broken = 0
    while rings:
        item_number, item_count = min_count(frequency_of_rings(rings))
        save_rings.append(item_number)
        # find connected rings
        connected = [connect for connect in rings if item_number in connect]
        # break this rings
        for ring_no in connected:
            for next_ring in list(ring_no):
                if next_ring == item_number:
                    continue
                else:
                    rings = [ring_connection for ring_connection in rings if next_ring not in ring_connection]
            rings_broken += 1
            print(rings_broken)
        
    return rings_broken

def min_count(rings):
    min = None
    
    for item in rings.items():
        if min is None or min[1] >= item[1]:
            min = item
    return min

def max_count(rings):
    max = (0, 0)
    
    for item in rings.items():
        if max[1] < item[1]:
            max = item
    return max
    
def frequency_of_rings(rings):
    count_dict = dict()
    
    for first, second in rings:
        count_dict[first] = count_dict.get(first, 0) + 1
        count_dict[second] = count_dict.get(second, 0) + 1
    
    return count_dict
  

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
    assert break_rings(({1,2},{2,3},{3,4},{4,5},{5,2},{1,6},{6,7},{7,8},{8,9},{9,6},{1,10},{10,11},{11,12},{12,13},{13,10},{1,14},{14,15},{15,16},{16,17},{17,14},)) == 8, "Long chain"
