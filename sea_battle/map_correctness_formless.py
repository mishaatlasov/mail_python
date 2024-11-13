import sys


def traverse(r, c, mp):
    global counter
    if not vis[r][c]:
        if mp[r][c] == "." and mp[r - 1][c] == "." and mp[r + 1][c] == "." and mp[r + 1][c + 1] == "." and mp[r - 1][c - 1] == "." and mp[r][c - 1] == "." and mp[r][c + 1] == "." and mp[r + 1][c - 1] == "." and mp[r - 1][c + 1] == ".":
            counter += 1
            vis[r][c] = True
            traverse(r + 1, c, mp)
            traverse(r, c + 1, mp)
            traverse(r - 1, c, mp)
            traverse(r, c - 1, mp)


R, C = map(int, input().split())
dots_string = "." * (C + 2)
map_ships = [list(dots_string)]

for j in range(0, R):
    map_ships.append(list("." + str(input()) + "."))

map_ships.append(list(dots_string))
for r in map_ships:
    print(''.join(r))
vis = [[False for c in range(C + 2)] for r in range(R + 2)]
counter = 0
max_counter = 0
sys.setrecursionlimit(50000)
for j in range(1, len(map_ships)):
    for i in range(1, len(map_ships[1])):
        if not vis[j][i] and map_ships[j][i] == ".":
            counter = 0
            traverse(j, i, map_ships)
            if counter > max_counter:
                max_counter = counter
            counter = 0
print(max_counter)