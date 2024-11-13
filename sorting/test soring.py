def usual_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def bucket_sort(array):
    n = len(array)
    buckets = [[] for _ in range(n)]
    max_value = max(array)

    for num in array:
        j = int(n * (num / max_value))
        if j == n:
            j = n - 1
        buckets[j].append(num)

    for i in range(n):
        usual_sort(buckets[i])

    ind = 0
    for bucket in buckets:
        for num in bucket:
            array[ind] = num
            ind += 1
    return arr
arr = [926, 178, 590, 469, 143, 215, 622, 743, 988, 309, 119, 405, 107, 433, 238, 440, 478, 837, 361, 814, 
       624, 497, 656, 789, 597, 355, 743, 995, 968, 820, 683, 440, 486, 677, 403, 983, 752, 370, 524, 569, 
       436, 101, 808, 222, 449, 877, 128, 993, 618, 165, 565, 849, 591, 956, 280, 341, 475, 712, 769, 225, 
       736, 681, 462, 545, 604, 771, 139, 311, 374, 632, 522, 844, 896, 319, 271, 728, 508, 226, 604, 607, 
       152, 147, 440, 294, 589, 903, 155, 489, 239, 812, 119, 498, 706, 481, 816, 585, 720, 947, 658, 564]

print(bucket_sort(arr))
