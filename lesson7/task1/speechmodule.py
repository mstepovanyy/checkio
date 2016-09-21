FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    handred = number // 100
    ten = (number % 100) // 10
    first = number % 10
    
    result = []
    
    if handred:
        result.append(FIRST_TEN[handred - 1])
        result.append(HUNDRED)
    

    if ten == 1:
        result.append(SECOND_TEN[first])
        return ' '.join(result)
    elif ten:
        result.append(OTHER_TENS[ten - 2])
    
    if first:
        result.append(FIRST_TEN[first - 1])

    return ' '.join(result)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
