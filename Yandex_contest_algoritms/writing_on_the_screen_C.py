

def traverse(r, c, mp):
    global counter
    if mp[r][c] == '#' and not vis[r][c]:
        vis[r][c] = True
        if mp[r + 1][c] in ('.', "£") and mp[r][c - 1] in ('.', "£"):
            print("the LB corner is", r, c)
            ships_corns.append([r, c])
        if mp[r - 1][c] in ('.', "£")  and mp[r][c + 1] in ('.', "£"):
            print("the RT corner is", r, c)
            ships_corns.append([r, c])

        counter += 1
        traverse(r + 1, c, mp)
        traverse(r, c + 1, mp)
        traverse(r - 1, c, mp)
        traverse(r, c - 1, mp)

S = int(input())
R, C = S, S
dots_string = "£" * (C + 2)
map_ships = [list(dots_string)]
for j in range(0, R):
    map_ships.append(list("£" + str(input()) + "£"))
print(R, C, map_ships)

map_ships.append(list(dots_string))
vis = [[False for c in range(C + 2)] for r in range(R + 2)]
counter = 0
ships = []
ships_corns = []
for j in range(len(map_ships)):
    for i in range(len(map_ships[1])):
        if not vis[j][i] and map_ships[j][i] == "#":
            counter = 0
            traverse(j, i, map_ships)
            ships.append(counter)

print(ships)
print(ships_corns)
if len(ships) == 1:
    global mp
    if map_ships[ships_corns[0][0] + 1][ships_corns[0][1]] == '.' and map_ships[ships_corns[0][0]][ships_corns[0][1] - 1] == '.' and map_ships[ships_corns[1][0] - 1][ships_corns[1][1]] == '.' and map_ships[ships_corns[1][0]][ships_corns[1][1] + 1] == '.':
        print("So this is 'O'")
