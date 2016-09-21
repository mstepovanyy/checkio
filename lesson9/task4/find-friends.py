

def create_network(network_, name, group):
    for items in network_:
        if name in items:
            if items[0] == name:
                if items[1] not in group:
                    group.add(items[1])
                    create_network(network_, items[1], group)
            else:
                if items[0] not in group:
                    group.add(items[0])
                    create_network(network_, items[0], group)
                    
def check_connection(network, first, second):
    
    #generate set of users
    group = set()
    
    network_ = [item.split('-') for item in network]
    create_network(network_, first, group)

    return second in group


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
