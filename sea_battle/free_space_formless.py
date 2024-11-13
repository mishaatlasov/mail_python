import sys


def traverse(r, c, mp):
    global counter
    global max_counter
    if r != 0 and r != len(map_ships) - 1 and c != 0 and c != len(map_ships[1]) - 1 and not vis[r][c]:
        vis[r][c] = True
        if mp[r][c] == "." and mp[r - 1][c] == "." and mp[r + 1][c] == "." and mp[r + 1][c + 1] == "." and mp[r - 1][c - 1] == "." and mp[r][c - 1] == "." and mp[r][c + 1] == "." and mp[r + 1][c - 1] == "." and mp[r - 1][c + 1] == ".":
            counter += 1
            all_counters.append(counter)
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
vis = [[False for c in range(C + 2)] for r in range(R + 2)]
counter = 0
max_counter = 0
all_counters = []
sys.setrecursionlimit(50000)
for j in range(len(map_ships)):
    for i in range(len(map_ships[1])):
        if not vis[j][i] and map_ships[j][i] == ".":
            traverse(j, i, map_ships)
            counter = 0
            all_counters.append(counter)
print(max_counter, all_counters)