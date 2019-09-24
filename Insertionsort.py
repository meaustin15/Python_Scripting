nums = [5,7,3,5,6,2,8]

def insertionsort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j], arr[j+1]
    return arr

print(insertionsort(nums))

