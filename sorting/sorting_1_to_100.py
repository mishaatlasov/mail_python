from arr_setup import arr
numbs_count = [0] * 101
sorted_list = []
for g in arr:
    numbs_count[g] += 1
for i in range(100):
    sorted_list.extend([i] * numbs_count[i])
    for _ in range(numbs_count[i]):
        sorted_list.append(i)
print(sorted_list)

