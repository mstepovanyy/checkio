def clock_angle(time):
    hours, minutes = time.split(":")
    m = int(minutes)
    h = int(hours) if int(hours) < 12 else int(hours) - 12
    deg_h = 360 / 12
    deg_hm = deg_h / 60
    deg_m = 360 / 60
    deg = max(deg_h * h + deg_hm * m, deg_m * m) - min(deg_h * h + deg_hm * m, deg_m * m)
    return deg if deg <= 180 else 360 - deg

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
