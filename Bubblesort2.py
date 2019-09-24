nums = [5,7,9,2,3]
print(nums)
def bubblesort(arr):
    for x in range(len(arr)-1,0,-1):
        for y in range(x):
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]
    return arr
print(bubblesort(nums))