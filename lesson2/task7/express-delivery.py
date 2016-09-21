def checkio(field_map):
    c_point = (0, 0)
    e_point = (len(field_map) - 1, len(field_map[0]) - 1)    
    # shortest way without drop box
    nodes = get_path(field_map, c_point, e_point, 2)
    drop_box = get_db(field_map)

    
    s_db = sorted(drop_box, key=lambda x:nodes[x]) [:2]
    
    e_nodes = get_path(field_map, e_point, c_point, 2)
    e_db = sorted(drop_box, key=lambda x:e_nodes[x]) [:2] 
    
    #path
    current_min = nodes[e_point]
    db_nodes = []
    for s in s_db:
        for e in e_db:
            s_value = nodes[s]
            e_value = e_nodes[e]
            db_value = get_path(field_map, s, e, 1)[e]
            length = s_value + e_value + db_value + 2
            if length < current_min:
                current_min = length
                db_nodes = (s, e)
    if db_nodes:
        road = get_road(field_map, nodes, db_nodes[0], c_point)
        road += 'B'
        road += get_road(field_map, get_path(field_map, db_nodes[0], db_nodes[1], 1), db_nodes[1], db_nodes[0])
        road += 'B'
        road += get_road(field_map, get_path(field_map, db_nodes[1], e_point, 1), e_point, db_nodes[1])
    else:
        road = get_road(field_map, nodes, e_point, c_point)

    return road

def get_road(field_map, nodes, s_point, e_point):
    ACTIONS = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
    }
    result = ''
    c_point = s_point
    while c_point != e_point:
        cell = get_available(field_map, c_point)
        
        step = min(cell, key=lambda x:nodes[x])
        move = (c_point[0] - step[0], c_point[1] - step[1])
        for label, move_t in ACTIONS.items():
            if move_t == move:
                result += label
        c_point = step
    return result[::-1]

def get_db(field_map):
    db = []
    for row in range(0, len(field_map)):
        for column in range(0, len(field_map[0])):
            if field_map[row][column]== 'B' and get_available(field_map, (row, column)):
                db.append((row, column))
    return db
            

def get_path(field_map, c_point, e_point, weight=2):
    nodes = {c_point: 0}
    l_cell = [c_point]

    visited = []
    #drop_box = []
    
    while l_cell:
        next_cell = l_cell
        l_cell = []
        for p in next_cell:
            if p in visited:
                continue
            cells = get_available(field_map, p)
            visited.append(p)
            #if field_map[p[0]][p[1]] == 'B':
            #    drop_box.append(p)

            for cell in cells:
                if cell in visited:
                    continue
                if nodes.get(cell, 999) > nodes[p] + weight:
                    nodes[cell] = nodes[p] + weight
            
            l_cell.extend(cells)
    return nodes
    

    


def get_available(field_map, point):
    x_max = len(field_map[0])
    y_max = len(field_map)
    ACTIONS = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
    }
    y, x = point
    available = []
    for move_y, move_x in ACTIONS.values():
        if (0 <= y + move_y < y_max) and (0 <= x + move_x < x_max) and field_map[y + move_y][x + move_x] != 'W':
            available.append((y + move_y,x + move_x))
    return available
        

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    ACTIONS = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
        "B": (0, 0)
    }

    def check_solution(func, max_time, field):
        max_row, max_col = len(field), len(field[0])
        s_row, s_col = 0, 0
        total_time = 0
        hold_box = True
        route = func(field[:])
        for step in route:
            if step not in ACTIONS:
                print("Unknown action {0}".format(step))
                return False
            if step == "B":
                if hold_box:
                    if field[s_row][s_col] == "B":
                        hold_box = False
                        total_time += 1
                        continue
                    else:
                        print("Stephan broke the cargo")
                        return False
                else:
                    if field[s_row][s_col] == "B":
                        hold_box = True
                    total_time += 1
                    continue
            n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
            total_time += 2 if hold_box else 1
            if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
                print("We've lost Stephan.")
                return False
            if field[n_row][n_col] == "W":
                print("Stephan fell in water.")
                return False
            s_row, s_col = n_row, n_col
            if field[s_row][s_col] == "E" and hold_box:
                if total_time <= max_time:
                    return True
                else:
                    print("You can deliver the cargo faster.")
                    return False
        print("The cargo is not delivered")
        return False
    
    assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
    assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"
    