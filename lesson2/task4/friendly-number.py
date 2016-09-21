import math
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    result = ''
    count = 0
    
    while abs(number)  >= base and len(powers) - 1 > count:
        count += 1
        number = number / base


    if number < 0:
        if decimals == 0:
            number = math.ceil(number * 10**decimals) / 10**decimals
        else:
            number = round(number, decimals)
    else:
        if decimals == 0 and len(str(number)) < 10:
            number = math.floor(number * 10**decimals )/10**decimals
        else:
            number = round(number, decimals )

    res = "{0:.{decim}f}".format(number, decim=decimals) if isinstance(number, float) or decimals else str(number)
    return res + powers[count] + suffix

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix="iB") == '976MiB', '976MiB'
    assert friendly_number(10**32) == '100000000Y', '100000000Y'

