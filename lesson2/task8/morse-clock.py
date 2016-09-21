def checkio(time_string):
    pattern = ["{0:04b}".format(item).replace('0','.').replace('1', '-') for item in range(10)]
    hour, minutes, seconds = time_string.split(':')
    hour = hour if len(hour) == 2 else '0'+ hour
    minutes = minutes if len(minutes) == 2 else '0'+ minutes
    seconds = seconds if len(seconds) == 2 else '0'+ seconds
    
    return pattern[int(hour[0])][2:] + ' ' + pattern[int(hour[1])] + ' : ' + \
        pattern[int(minutes[0])][1:] + ' ' + pattern[int(minutes[1])] + ' : ' + \
        pattern[int(seconds[0])][1:] + ' ' + pattern[int(seconds[1])]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

