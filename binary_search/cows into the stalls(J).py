def check(stalls_cords, cows, mid):
    counter = 0
    occupied_stalls = []
    shadow_stalls = [False * len(stalls_cords)]
    while counter < cows:
        counter += 1
        if len(occupied_stalls) == 0:
            shadow_stalls[0] = True
            occupied_stalls.append(stalls_cords[0])
        if len(occupied_stalls) == 1:
            shadow_stalls[-1] = True
            occupied_stalls.append(stalls_cords[-1])
        if len(occupied_stalls) >= 2:
            pass


stalls, cows = map(int, input().split())
stalls_cords = input().split()
for j in range(len(stalls_cords)):
    stalls_cords[j] = int(stalls_cords[j])


left, right = 1, stalls_cords[-1]
while right - left > 1:
    mid = (left + right) // 2
    if check(stalls_cords, cows):
        right = mid
    else:
        left = mid
print(right)