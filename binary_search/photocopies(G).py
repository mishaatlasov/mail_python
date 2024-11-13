def check(amount, fm, sm, mid):
    return ((mid - min(fm, sm)) // fm) + ((mid - min(fm, sm)) // sm) >= amount - 1


amount, fm, sm = map(int, input().split())


left, right = 1, min(fm, sm) * (amount + 2)
while right - left > 1:
    mid = (left + right) // 2
    if check(amount, fm, sm, mid):
        right = mid
    else:
        left = mid
print(right)
