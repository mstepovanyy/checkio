def finish_map(regional_map):
    start_points = []
    regional_map = [list(item) for item in regional_map]
    for r_id, row in enumerate(regional_map):
        for c_id, column in enumerate(row):
            if column == '.':
                regional_map[r_id][c_id] = 'S'
            elif column == 'D':
                start_points.append((r_id, c_id))
    mark_danger(regional_map, start_points)
    return ["".join(item) for item in regional_map]

def mark_danger(r_map, start_points):
    for point in start_points:
        # get_all_moves for `point`
        while True:
            possible_moves = get_possible(r_map, point)
            
            for move in possible_moves:
                r_map[move[0]][move[1]] = 'D'
            
            # implement checker
            if possible_moves:
                mark_danger(r_map, possible_moves)
            else:
                break

def get_possible(r_map, point):
    raw_map = get_raw_moves(r_map, point, around=False)
    danger = []
    for point in raw_map:
        moves = get_raw_moves(r_map, point)
        if is_danger(r_map, moves):
            danger.append(point)
    
    return [item for item in danger if r_map[item[0]][item[1]] != 'D']

def is_danger(r_map, points):
    return len([p for p in points if r_map[p[0]][p[1]] == 'X']) == 0
    

def get_raw_moves(r_map, p, around=True):
    if  around:
        moves = ((-1, -1), (-1, 0),(-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    else:
        moves = ( (-1, 0), (0, -1), (0, 1),  (1, 0), )
    return [(p[0]+i[0], p[1]+i[1]) for i in moves if 0 <= p[0]+i[0] < len(r_map) and 0 <= p[1] + i[1] < len(r_map[0])]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(finish_map(("..........",".D.......X","..........","..........",
                            "......X...","..........","..........","...X......",
                            "..........","..........","X.........")))==["DDDDDDDDSS","DDDDDDDDSX","DDDDDDDDSS","DDDDDSSSSS","DDDDDSXSSS","DDDDDSSSSS","DDSSSSSSSS","DDSXSSSSSS","DDSSSSSSSS","SSSSSSSSSS","XSSSSSSSSS"], "Broken"
    assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"
