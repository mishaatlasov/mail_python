n = []
for g in range(6):
    n.append(int(input()))
x1, y1, x2, y2, x, y = n[0], n[1], n[2], n[3], n[4], n[5]

def Get_the_swimmer_to_the_fleet(x1, y1, x2, y2, x, y):
    if y > y1 and y < y2:
        if x < x1:
            return "W"
        if x > x2:
            return "E"
    elif x > x1 and x < x2:
        if y < y2:
            return "S"
        if y > y1:
            return "N"
    elif y > y2:
        if x < x1:
            return "NW"
        if x > x2:
            return "NE"
    elif y < y1:
        if x < x1:
            return "SW"
        if x > x2:
            return "SE"

print(Get_the_swimmer_to_the_fleet(x1, y1, x2, y2, x, y))
