import math

def checkio(bunker):
    return pathfind(bunker, (0, 0))


def pathfind(bunker, point):
    nodes = dict()
    finish = ()
    visited = []
    for y in range(len(bunker)):
        for x in range(len(bunker[0])):
            if bunker[y][x] == 'B':
                nodes[(y,x)] = 9999
            elif bunker[y][x] == 'A':
                finish = (y,x)
                nodes[(y,x)] = 9999
    nodes[point] = 0
    connected_nodes = dict()
    
    for node in nodes.keys():
        for next in nodes.keys():
            if node == next:
                continue
            elif not is_wall(bunker, node, next):
                if node not in connected_nodes.keys():
                    connected_nodes[node] = set()
                connected_nodes[node].add(next)

    n_nodes = [(0,0),]
    while True:
        next_nodes = n_nodes
        if not next_nodes:
            break
        n_nodes = list()

        for cur_n in next_nodes:
            
            if cur_n in visited:
                continue
            if cur_n == finish:
                break

            for node in list(connected_nodes[cur_n]):
                visited.append(cur_n)
                dist = get_distance(cur_n, node)
                if nodes[node] > nodes[cur_n] + dist:
                    nodes[node] = nodes[cur_n] + dist
            n_nodes.extend(connected_nodes[cur_n])

    return nodes[finish]

            
def is_wall(bunker, p1, p2):
    coordinates = get_coordinates(get_cross(p1, p2))
    for y, x in coordinates:
        if bunker[y][x] == 'W':
            return True
    return False

def get_coordinates(points):
    coordinates = set()
    for y, x in points:
        if y == int(y) and x == int(x):
            coordinates.add((int(y),int(x)))
            coordinates.add((int(y) - 1, int(x)))
            coordinates.add((int(y), int(x) - 1))
            coordinates.add((int(y) - 1, int(x) - 1))
        elif y == int(y):
            coordinates.add((int(y), int(x)))
            coordinates.add((int(y) - 1, int(x)))
        elif x == int(x):
            coordinates.add((int(y), int(x)))
            coordinates.add((int(y), int(x) - 1))
    return coordinates

def get_cross(point1, point2):
    angle = get_angle(point1, point2)
    angle_y = math.radians(90 - math.degrees(angle))
    
    p1 = (point1[0] + 0.5, point1[1] + 0.5)
    
    cross_points = set()

    #can be optimized
    for x in range(point1[1] + 1, point2[1] + 1):
        distance_x = x - p1[1]
        distance_y = round(distance_x * math.tan(angle), 6)
        #print(point1, p1[0] + distance_y,  p1[1] + distance_x)
        cross_points.add( (p1[0] + distance_y, p1[1] + distance_x) )
    
    for x in range(point2[1] + 1, point1[1] + 1):
        distance_x = x - p1[1]
        distance_y = round(distance_x * math.tan(angle), 6)
        #print(point1, p1[0] + distance_y,  p1[1] + distance_x)
        cross_points.add( (p1[0] + distance_y, p1[1] + distance_x) )
        
    for y in range(point1[0] + 1, point2[0] + 1):
        distance_y = y - p1[0]
        distance_x = round(distance_y * math.tan(angle_y), 6)
        #print(point1, p1[0] + distance_y,  p1[1] + distance_x )
        cross_points.add( (p1[0] + distance_y, p1[1] + distance_x) )
        
    for y in range(point2[0] + 1, point1[0] + 1):
        distance_y = y - p1[0]
        distance_x = round(distance_y * math.tan(angle_y), 6)
        #print(point1, p1[0] + distance_y,  p1[1] + distance_x )
        cross_points.add( (p1[0] + distance_y, p1[1] + distance_x) )
    
    return cross_points
        
    

def get_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
    
    
def get_angle(point1, point2):
    angle = math.atan2(point2[0] - point1[0], point2[1] - point1[1])

    return angle

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([
        "B--",
        "-B-",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"
