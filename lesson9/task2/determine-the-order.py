def checkio(data):
    result = dict()
    
    for word in data:
        prev_ = ''
        for value, letter in enumerate(word):
            power = result.get(letter,[])
            if value == 0:
                power.append(1)
            elif letter == word[value - 1]:
                continue
            else:
                power.append(word[value - 1])
                power.append(1)
            result[letter] = power
   
    for letter, val in result.items():
        if isinstance(val, int):
            pass
        else:
            get_number(result, letter)
    res = sorted(result.items(), key=lambda x: (x[1], x[0]))
    join = "".join(data)
    if len(res) == len(join):
        return "".join(sorted(join))
        
    
    return "".join([letter[0] for letter in res ])
    

def get_number(result, letter):
    
    number = result[letter]
    if isinstance(number, int):
        return number
    else:
        sum = 0
        for item in number:
            if isinstance(item, int):
                sum += item
            else:
                sum += get_number(result, item)
        result[letter] = sum
        return sum    
    
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
