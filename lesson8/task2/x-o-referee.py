def checkio(game_result):
    
    possible_lines = game_result
    
    possible_lines.append(game_result[0][0] + game_result[1][0] + game_result[2][0])
    possible_lines.append(game_result[0][1] + game_result[1][1] + game_result[2][1])
    possible_lines.append(game_result[0][2] + game_result[1][2] + game_result[2][2])
    possible_lines.append(game_result[0][0] + game_result[1][1] + game_result[2][2])
    possible_lines.append(game_result[0][2] + game_result[1][1] + game_result[2][0])
    
    
    for line in possible_lines:
        if line.count('X') == 3:
            return 'X'
        if line.count('O') == 3:
            return 'O'
    return "D" 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

