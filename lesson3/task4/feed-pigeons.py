def checkio(number):
        
    def food_left(food, pigions, minute):
        if food > pigions:
            minute += 1
            return food_left(food - pigions, pigions + minute, minute)
        else:
            return max(pigions - minute, food)
    
    return food_left(number, 1, 1)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"