numbers = [99, 44, 6, 2, 1, 5, 63, 87, 4, 0, 283]


def insertionSort(arr):
    length = len(arr)
    for i in range(length):
        if arr[i] < arr[0]:
            # move to first position
            arr.insert(0, arr[i])
            del arr[i+1]
        else:
            # find where the num should go
            for j in range(1, i):
                if arr[i] > arr[j-1] and arr[i] < arr[j]:
                    # move the item
                    arr.insert(j, arr[i])
                    del arr[i+1]
    print(arr)


insertionSort(numbers)
