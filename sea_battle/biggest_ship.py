vysota, dlinna = input().split()
vysota, dlinna = int(vysota), int(dlinna)
dots_string = "." * (dlinna + 2)
map_ships = [dots_string]

for i in range(0, vysota):
    map_ships.append("." + str(input()) + ".")
map_ships.append(dots_string)
vysota, dlinna = vysota + 2, dlinna + 2


def read_all_field(field):
    max_counter = 0
    height, length = len(field), len(field[0])
    for r in range(height):
        for c in range(length):
            counter_c = 0
            counter_r = 0
            if field[r][c] == "#" and field[r][c - 1] == "." and field[r - 1][c] == ".":
                x = 0
                while field[r + x][c] == "#":
                    x += 1
                    counter_r += 1
                x = 0
                while field[r][c + x] == "#":
                    x += 1
                    counter_c += 1
            max_counter = max(max_counter, counter_r, counter_c)

    return max_counter


print(read_all_field(map_ships))
