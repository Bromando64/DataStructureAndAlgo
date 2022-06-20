numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubbleSort(arr):
    length = len(arr) - 1
    for i in range(length):
        for j in range(length):
            if arr[j] > arr[j+1]:
                # swap numbers
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


print(bubbleSort(numbers))
