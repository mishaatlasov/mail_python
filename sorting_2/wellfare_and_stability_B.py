n = int(input())
a = []
for j in range(n):
    a.append(input().split())
    a[j][1] = int(a[j][1])
    a[j][2] = int(a[j][2])
    a[j][3] = int(a[j][3])
for j in range(n):
    a[j].append(a[j][1] + (a[j][2] * 5) + (a[j][3] * 7))
j = sorted(a, key=lambda x: x[4], reverse=True)
for k in range(n):
    print(j[k][0])