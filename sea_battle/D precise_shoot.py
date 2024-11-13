def precise_shoot():
    vysota, dlinna = input().split()
    vysota, dlinna = int(vysota), int(dlinna)
    forbidden_string = "." * (dlinna + 2)
    map_ships = []
    for i in range(0, vysota):
        map_ships.append([])
        map_ships[i].append("." + str(input()) + ".")
    vysterl_vertik, vysterl_gorizont = input().split()
    vysterl_vertik, vysterl_gorizont = int(vysterl_vertik), int(vysterl_gorizont)
    map_ships.insert(0, [forbidden_string])
    map_ships.insert(vysota + 1, [forbidden_string])
    vysota, dlinna = vysota + 2, dlinna + 2
    if map_ships[vysterl_vertik][0][vysterl_gorizont] != "#":
        for i in range(1, vysota - 1):
            print(map_ships[i][0])

    visited = []
    visited_first = [[False] * dlinna]
    for i in range(vysota):
        visited += visited_first

    def explore(field, visited, vertikal, gorizontal):
        visited[vertikal][gorizontal] = True
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dr, dc in dirs:
            new_vertikal, new_gorizontal = vertikal + dr, gorizontal + dc
            if not (0 <= new_vertikal < vertikal) or not (0 <= new_gorizontal < gorizontal):
                continue
            if map_ships[new_vertikal][0][new_gorizontal] == "#":
                map_ships[new_vertikal][0][new_gorizontal].replace("#", ".")
            if not visited[new_vertikal][new_gorizontal]:
                explore(field, visited, new_vertikal, new_gorizontal)
    explore(map_ships, visited, vysterl_vertik, vysterl_gorizont)
    for i in range(1, vysota - 1):
        print(map_ships[i][0])
precise_shoot()
