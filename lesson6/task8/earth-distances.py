R = 6371
import math, re

def distance(first, second):
    lat1, long1 = re.split("[,\s]+", first)
    lat2, long2 = re.split("[,\s]+", second)
    
    f1 = math.radians(to_float(lat1))
    f2 = math.radians(to_float(lat2))
    d_lat =math.radians(to_float(lat2) - to_float(lat1))
    d_long = math.radians(to_float(long2) - to_float(long1))
    
    a = math.sin(d_lat/2) ** 2 + math.cos(f1) * math.cos(f2) * math.sin(d_long/2) ** 2

    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def to_float(value):
    grad, minutes, seconds = re.match("(\d+)°(\d+)′(\d+)″", value).groups()
    grad = float(grad) + float(minutes)/60 + float(seconds)/3600
    if 'S' in value or 'W' in value:
        grad = grad - grad * 2
    return grad

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
