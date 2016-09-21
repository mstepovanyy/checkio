def safe_pawns(pawns):
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'out']
    rows = ['1', '2', '3', '4', '5', '6', '7', '8']
    
    result = 0
    
    for pawn in pawns:
        column, row = pawn[0], pawn[1]
        
        r_index = rows.index(row)
        if r_index == 0:
            continue
        row_number = rows[r_index - 1]
        
        c_index = columns.index(column)
        left_column, right_column = columns[c_index - 1], columns[c_index + 1]
        

        if left_column + row_number in pawns or right_column + row_number in pawns:
            result += 1
    
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
