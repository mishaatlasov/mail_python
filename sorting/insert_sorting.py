# getting info about list
v = int(input())
arr = input().split()

for j in range(v):
    arr[j] = int(arr[j])


for g in range(1, v):
    if g > 0 and arr[g - 1] > arr[g]:
        while g > 0 and arr[g - 1] > arr[g]:
            arr[g], arr[g - 1] = arr[g - 1], arr[g]
            g -= 1
        for i in arr:
            print(i, end=' ')
        print("")
