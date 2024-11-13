n_len, k_len = input().split()
n_len, k_len = int(n_len), int(k_len)
n_list = input().split()
k_list = input().split()
for j in range(0, n_len):
    n_list[j] = int(n_list[j])
for h in range(0, k_len):
    k_list[h] = int(k_list[h])


def left_binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    if left < len(arr) and arr[left] == target:
        return left
    return -1


def right_binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    if arr[left - 1] == target:
        return left
    else:
        return 0


for q in range(len(k_list)):
    if left_binary_search(n_list, k_list[q]) + 1 != 0:
        print(left_binary_search(n_list, k_list[q]) + 1, right_binary_search(n_list, k_list[q]))
    else:
        print(0)
