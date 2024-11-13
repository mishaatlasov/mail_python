a = input().split()
j = sorted(a, key=lambda x: x[::-1])
print(" ".join(j))