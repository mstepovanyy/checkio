def battle_probability(dice_description, units_one, units_two):
    return 0.0

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(battle_probability(['A', 'D'], 3, 3), 0.0000)), "Always ties, nobody wins"
    assert(almost_equal(battle_probability(['A', 'D'], 4, 3), 1.0000)), "Always win"
    assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 3, 4), 0.0186)), "You can win"
    assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 4, 4), 0.4079)), "Ready to fight"
    assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 5, 4), 0.9073)), "I have good chance"
