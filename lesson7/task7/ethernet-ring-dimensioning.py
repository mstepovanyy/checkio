ETHERNET = (100, 40, 10, 1, 0.1) # Ethernet bandwidth capacity in Gbps

def checkio(ring, *flows):
    pass

if __name__ == '__main__':
    # These "asserts" are used only for self-checking and not necessary for auto-testing
    assert checkio("AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]
