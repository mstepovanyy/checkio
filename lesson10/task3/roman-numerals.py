def checkio(data):
    one_l = ('M', 'C', 'X', 'I')
    ten_l = ('undefined', 'M', 'C', 'X')
    five_l = ('undefined', 'D', 'L', 'V')
    
    power = 3
    result = ''
    
    for one, ten, five in zip(one_l, ten_l, five_l):
        number = data // (10**power)
        data = data % (10**power)
        if number < 4:
            result += one * number
        elif number == 4:
            result += one + five
        elif number == 9:
            result += one + ten
        else: # in range 5 - 8
            result += five + one * (number - 5)
        
        power -= 1   
    
    #replace this for solution
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'