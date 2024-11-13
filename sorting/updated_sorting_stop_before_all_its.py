from arr_setup import arr
import time
start = time.time()


def bubble_sort(arr):
    itt = 0
    swapped = True
    while swapped:
        swapped = False

        for i in range(len(arr) - 1):
            itt += 1
            if arr[i] > arr[i + 1]:


                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        for j in range(len(arr) - 1, 0, -1):
            itt += 1
            if arr[j] < arr[j - 1]:

                swapped = True
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        if not swapped:
            print(itt)
            return arr

print(bubble_sort(arr))
end = time.time()
print(end-start)