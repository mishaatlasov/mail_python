k = int(input())
list_1 = input().split()
for j in range(0, k):
    list_1[j] = int(list_1[j])


def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


list_1 = bubble_sort(list_1)
for i in list_1:
    print(i, end=' ')