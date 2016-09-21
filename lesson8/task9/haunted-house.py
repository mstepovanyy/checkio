
iteration=0
def checkio(house, stephan, ghost):
    exit = 1
    nodes = {item: 999 for item in range(1, 17)}
    nodes[stephan] = 0
    unvisited = list(range(1,17))
    
    next_nodes = [stephan, ]
    while next_nodes:
        
        row = []
        for c_id in next_nodes:
            
            if c_id in unvisited:
                unvisited.remove(c_id)
            else:
                continue
            # find all the nodes next to current
            cells = get_cells(house, c_id)
            row.extend(cells)
            
            #calculate value for this node
            for id in cells:
                if nodes[id] > nodes[c_id] + 1:
                    nodes[id] = nodes[c_id] + 1
        next_nodes = row

    #create two possible paths
    c_node = 1
    first_path = [c_node,]
    
    while c_node != stephan:
        
        possible_ways = get_cells(house, c_node)
        possible_ways.sort(key=lambda x:nodes[x])
        
        c_node = possible_ways[0]
        first_path.append(c_node)
    
    c_node = 1
    second_path = [c_node,]
    different = False
    while c_node != stephan:
        possible_ways = get_cells(house, c_node)
        possible_ways.sort(key=lambda x:nodes[x])
        nodes[c_node] = 999
        if len(possible_ways) == 1:
            second_path.append(possible_ways[0])
            c_node = possible_ways[0]
        else:
            path_l = len(second_path)
            if first_path[:path_l] == second_path:
                
                if first_path[path_l - 1] != possible_ways[0]:

                    c_node = possible_ways[1]
                else:
                    c_node = possible_ways[0]
            else:
                c_node = possible_ways[0]
            second_path.append(c_node)

    
    possible_moves = {"N": -4, "S": 4, "E": 1, "W": -1}
    
    if len(first_path) == 1:
        return 'N'
    global iteration
    iteration += 1
    if iteration > 3:
        move = first_path[-2] - first_path[-1]
    else:
        return 'W' if iteration % 2 else 'E'
    if (ghost in first_path and ghost in second_path) or ghost in first_path:
        move = second_path[-2] - second_path[-1]
    elif ghost in second_path:
        move = first_path[-2] - first_path[-1]
    else:
        move = first_path[-2] - first_path[-1]
    
    letter = [key for key, value in possible_moves.items() if value == move]
    return letter[0]
    
def get_cells(house, number, ghost=None):
    walls = house[number-1]
    possible_moves = {"N": -4, "S": 4, "E": 1, "W": -1}
    for wall in walls:
        del possible_moves[wall]
    
    #remove moved throught table boarder
    if number % 4 == 0:
        del possible_moves['E']
    if number <= 4:
        del possible_moves['N']
    if number % 4 == 1:
        del possible_moves['W']
    if number >= 13:
        del possible_moves['S']
        
            
    return [number + value for value in possible_moves.values() if 0 < number + value <= 16]

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    from random import choice

    DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}

    def check_solution(func, house):
        stephan = 16
        ghost = 1
        for step in range(30):
            direction = func(house[:], stephan, ghost)
            if direction in house[stephan - 1]:
                print('Stefan ran into a closed door. It was hurt.')
                return False
            if stephan == 1 and direction == "N":
                print('Stefan has escaped.')
                return True
            stephan += DIRS[direction]
            if ((direction == "W" and stephan % 4 == 0) or (direction == "E" and stephan % 4 == 1) or
                    (stephan < 1) or (stephan > 16)):
                print('Stefan has gone out into the darkness.')
                return False
            sx, sy = (stephan - 1) % 4, (stephan - 1) // 4
            ghost_dirs = [ch for ch in "NWES" if ch not in house[ghost - 1]]
            if ghost % 4 == 1 and "W" in ghost_dirs:
                ghost_dirs.remove("W")
            if not ghost % 4 and "E" in ghost_dirs:
                ghost_dirs.remove("E")
            if ghost <= 4 and "N" in ghost_dirs:
                ghost_dirs.remove("N")
            if ghost > 12 and "S" in ghost_dirs:
                ghost_dirs.remove("S")

            ghost_dir, ghost_dist = "", 1000
            for d in ghost_dirs:
                new_ghost = ghost + DIRS[d]
                gx, gy = (new_ghost - 1) % 4, (new_ghost - 1) // 4
                dist = (gx - sx) ** 2 + (gy - sy) ** 2
                if ghost_dist > dist:
                    ghost_dir, ghost_dist = d, dist
                elif ghost_dist == dist:
                    ghost_dir += d
            ghost_move = choice(ghost_dir)
            ghost += DIRS[ghost_move]
            if ghost == stephan:
                print('The ghost caught Stephan.')
                return False
        print("Too many moves.")
        return False

    assert check_solution(checkio,
                          ["", "S", "S", "",
                           "E", "NW", "NS", "",
                           "E", "WS", "NS", "",
                           "", "N", "N", ""]), "1st example"
    assert check_solution(checkio,
                          ["", "", "", "",
                           "E", "ESW", "ESW", "W",
                           "E", "ENW", "ENW", "W",
                           "", "", "", ""]), "2nd example"
