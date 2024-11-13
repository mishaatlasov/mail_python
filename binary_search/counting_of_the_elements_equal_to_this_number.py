def left_binary_search(arr, target):
    left, right = -1, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            left = mid
        else:
            right = mid
    return right


def right_binary_search(arr, target):
    left, right = 0, len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid
        else:
            right = mid
    return left


def closest_find(arr, target):
    if target <= arr[0]:
        return arr[0]
    if target >= arr[-1]:
        return arr[-1]
    left = right_binary_search(arr, target)
    ans = left + 1
    if target - arr[left] <= arr[ans] - target:
        ans -= 1
    return arr[ans]


n_len, k_len = input().split()
n_len, k_len = int(n_len), int(k_len)
n_list = input().split()
k_list = input().split()
for j in range(0, n_len):
    n_list[j] = int(n_list[j])
for h in range(0, k_len):
    k_list[h] = int(k_list[h])

for q in range(len(k_list)):
    print(closest_find(n_list, k_list[q]))
