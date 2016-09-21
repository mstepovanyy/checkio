import random

l_moves = ""

def checkio(puzzle):
    """
    Solve the puzzle
      U - up
      D - down
      L - left
      R - right
    """
    # set 1
    global l_moves
    l_moves = ""
    unmovable = []
    random_move(puzzle, {1:(0,0)}, unmovable)
    unmovable.append((0,0))
    
    random_move(puzzle, {3:(0,1)}, unmovable)
    unmovable.append((0,1))
    random_move(puzzle, {2:(1,1)}, unmovable)
    unmovable.append((1,1))
    # set top row
    random_move(puzzle, {0: (0,2)}, unmovable)
    unmovable.append((0,2))
    unmovable.remove((1,1))
    move_zero(puzzle, ('L',(0, -1)))
    move_zero(puzzle, ('D', (1, 0)))
    print(puzzle)
    
    
    random_move(puzzle, { 7: (1,0), 4:(1,1)} , unmovable)
    unmovable.append((1,0))
    unmovable.append((1,1))
    print(puzzle)
    random_move(puzzle, {0:(2,0)}, unmovable)
    unmovable.append((2,0))
    print(puzzle)
    
    # set left column
    move_zero(puzzle, ('U', (-1, 0)))
    move_zero(puzzle, ('R', (0, 1)))
    unmovable.remove((1,1))
    
    random_move(puzzle, {5:(1,1)}, unmovable)
    unmovable.append((1,1))
    random_move(puzzle, {6:(1,2)}, unmovable)
    unmovable.append((1,2))
    random_move(puzzle, {8:(2,1)}, unmovable)
    print(puzzle)
    useles_moves = ["LR", "RL", "UD", "DU", "LLRR", "RRLL", "UUDD", "DDUU"]
    
    
    while True:
        before = l_moves
        for move in useles_moves:
            l_moves = l_moves.replace(move, "")
        if before == l_moves:
            break
    return l_moves

# need to think about smarter move algorithm
def random_move(puzzle, expected_positions, unmovable):

    while not on_expected(puzzle, expected_positions):
        moves = get_possible(puzzle, unmovable)
        move = random.sample(moves, 1)
        move_zero(puzzle, move[0])

def on_expected(puzzle, expected):
    for number, point in expected.items():
        if puzzle[point[0]][point[1]] != number:
            return False
    return True
        

def road(puzzle, start, end):
    c_point = start
    while c_point != end:
        move_x = end[1] - c_point[1]
        move_y = end[0] - c_point[0]
        if move_x:
            next_point = c_point
            #next_point[1] += 
        
    
def get_position(puzzle, number):
    for r_n, row in enumerate(puzzle):
        for c_n, item in enumerate(row):
            if number == item:
                return r_n, c_n


    

def move_zero(puzzle, move):
    global l_moves
    l_moves += move[0]
    y,x = get_position(puzzle, 0)
    puzzle[y][x], puzzle[y+move[1][0]][x+move[1][1]] = puzzle[y+move[1][0]][x+move[1][1]], puzzle[y][x]
    # store move
    
def get_possible(puzzle, unmovable):
    z_point = get_position(puzzle, 0)
    MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    result = []
    for letter, move in MOVES.items():
        if  0 <= z_point[0] + move [0] <= 2 and 0 <= z_point[1] + move[1] <= 2 and (z_point[0] + move [0], z_point[1] + move[1]) not in unmovable:
            result.append((letter, move))
    return result
            
        
        
    
        

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def check_solution(func, puzzle):
        size = len(puzzle)
        route = func([row[:] for row in puzzle])
        goal = GOAL
        x = y = None
        for i, row in enumerate(puzzle):
            if 0 in row:
                x, y = i, row.index(0)
                break
        for ch in route:
            swap_x, swap_y = x + MOVES[ch][0], y + MOVES[ch][1]
            if 0 <= swap_x < size and 0 <= swap_y < size:
                puzzle[x][y], puzzle[swap_x][swap_y] = puzzle[swap_x][swap_y], 0
                x, y = swap_x, swap_y
        if puzzle == goal:
            return True
        else:
            print("Puzzle is not solved")
            return False

    assert check_solution(checkio, [[1, 2, 3],
                                    [4, 6, 8],
                                    [7, 5, 0]]), "1st example"
    assert check_solution(checkio, [[7, 3, 5],
                                    [4, 8, 6],
                                    [1, 2, 0]]), "2nd example"
