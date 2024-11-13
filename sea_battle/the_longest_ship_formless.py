import sys


def traverse(r, c, mp):
    global counter
    if mp[r][c] == '#' and not vis[r][c]:
        vis[r][c] = True
        counter += 1
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
sys.setrecursionlimit(50000)
counter = 0
max_counter = 0
for j in range(len(map_ships)):
    for i in range(len(map_ships[1])):
        if not vis[j][i] and map_ships[j][i] == "#":
            counter = 0
            traverse(j, i, map_ships)
            print(counter)

if max_counter == 0:
    print("No ships found")
else:
    print(max_counter)