numbers = [99, 44, 6, 2, 1, 5, 63, 87, 4, 0, 283]


def SelectionSort(arr):
    length = len(arr)
    for i in range(0, length):
        small = i
        temp = arr[i]
        for j in range(i+1, length):
            if arr[j] < arr[small]:
                small = j
        arr[i] = arr[small]
        arr[small] = temp
    print(arr)


SelectionSort(numbers)
