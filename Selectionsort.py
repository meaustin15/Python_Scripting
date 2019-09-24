nums = [5,1,6,8,3,9]

print(nums)

def selectionsort(arr):
    for x in range(len(arr)-1):
        minimum = min(arr[x:])

        if arr[x] > minimum:
            arr[arr.index(minimum)], arr[x] = arr[x], arr[arr.index(minimum)]

    return arr

print(selectionsort(nums))