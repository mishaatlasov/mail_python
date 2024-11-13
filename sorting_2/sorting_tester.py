n = int(input().strip())
array1 = list(map(int, input().strip().split()))
m = int(input().strip())
array2 = list(map(int, input().strip().split()))

if sorted(set(array1)) == sorted(set(array2)):
    print("YES")
else:
    print("NO")