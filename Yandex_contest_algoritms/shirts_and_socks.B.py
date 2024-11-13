from operator import indexOf

n = []
for g in range(4):
    n.append(int(input()))
shirts_b, shirts_r, socs_b, socs_r = n[0], n[1], n[2], n[3]
def find_optimal_way():
    mix_socks = [1, max(socs_b, socs_r) + 1]
    mix_shirts = [max(shirts_b, shirts_r) + 1, 1]
    get_all_blue = [shirts_r + 1, socs_r + 1]
    get_all_red = [shirts_b + 1, socs_b + 1]
    if socs_b == 0:
        print(shirts_b + 1 ,1)
        exit(0)
    elif socs_r == 0:
        print(shirts_r + 1 ,1)
        exit(0)
    elif shirts_b == 0:
        print(1, socs_b + 1)
        exit(0)
    elif shirts_r == 0:
        print(1, socs_r + 1)
        exit(0)
    sums = [sum(mix_socks), sum(mix_shirts), sum(get_all_blue), sum(get_all_red)]
    they_all = [mix_socks, mix_shirts, get_all_blue, get_all_red]
    print(they_all[indexOf(sums, min(sums))][0], they_all[indexOf(sums, min(sums))][1])
find_optimal_way()