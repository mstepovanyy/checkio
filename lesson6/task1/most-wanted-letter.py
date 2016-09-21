def checkio(text):

    import string
    
    res = dict()
    
    for letter in text.lower():
        if letter in string.ascii_lowercase:
            res[letter] = res[letter] + 1 if letter in res.keys() else 1

    max = ('a', 0)
    for key, value in res.items():
        if max[1] < value or max[1] == value and max[0] > key:
            max = (key, value)

#replace this for solution
    return max[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
