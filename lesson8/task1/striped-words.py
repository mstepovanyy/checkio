VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    count = 0
    text = text.replace(',', ' ').replace('.', ' ')
    for word in text.split():
        word = word.upper().strip('.,/?')
        if len(word) <= 1:
            continue
        
        if (set(word[::2]) <= set(VOWELS) and set(word[1::2]) <= set(CONSONANTS)) or (set(word[1::2]) <= set(VOWELS) and set(word[::2]) <= set(CONSONANTS) ):
            count += 1
            print(word)
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words.") == 6, "Dog, cat and human"
