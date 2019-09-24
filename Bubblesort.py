import random

randint = random.randint(0,10)

randarr = []

for x in range(5):
    randarr.append(random.randint(0,10))

# nums = [5,1,6,8,3,9]

print("Unsorted",randarr)

def bubblesort(arr):
    for x in range(len(arr)-1,0,-1):
        for y in range(x):
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]

    return arr

print("Sorted",bubblesort(randarr))



