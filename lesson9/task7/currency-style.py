def checkio(text):
    result = []
    for line in text.split('\n'):
        sentense = []
        for word in line.split(" "):
            digits = '0123456789'
            if len(word)>0 and word[0] == '$':
                last = word[-1]
                word = word.replace('.', ',')
                word = list(word)
                if last not in digits:
                    word[-1] = last
                    if len(word) > 4 and word[-4] not in digits:
                        word[-4] = '.'
                else:
                    if len(word) > 3 and word[-3] not in digits:
                        word[-3] = '.'
                sentense.append  ("".join(word))
            else:
                sentense.append(word)
        result.append(" ".join(sentense))
        
    return "\n".join(result)

if __name__ == '__main__':    
    assert checkio("Clayton Kershaw $31.000.000\nZack Greinke   $27.000.000\nAdrian Gonzalez $21.857.143\n")
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
    assert checkio("$0,89") == "$0.89" , "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9", "Dollars without cents"
