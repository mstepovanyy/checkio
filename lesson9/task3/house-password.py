def checkio(data):
    import string
    
    data_set = set(data)
    ascii_lowercase_set = set(string.ascii_lowercase)
    ascii_uppercase_set = set(string.ascii_uppercase)
    digits_set = set(string.digits)
    
    if ascii_lowercase_set & data_set and ascii_uppercase_set & data_set and digits_set & data_set and len(data) >= 10:
        return True

    #replace this for solution
    return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
