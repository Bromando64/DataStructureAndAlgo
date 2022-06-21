numbers = [99, 44, 6, 2, 1, 5, 63, 87, 4, 0, 283]
# MergeSort in Python


def mergeSort(array):
    if len(array) > 1:

        #  middle is the point where the array is divided into two subarrays
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]
        # Sort the two halves
        mergeSort(left)
        mergeSort(right)

        leftIndex = rightIndex = index = 0

        # Until we reach either end of either left or right, pick larger among
        # elements left and right and place them in the correct position at A[p..r]
        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                array[index] = left[leftIndex]
                leftIndex += 1
            else:
                array[index] = right[rightIndex]
                rightIndex += 1
            index += 1

        # When we run out of elements in either left or right,
        # pick up the remaining elements and put in A[p..r]
        while leftIndex < len(left):
            array[index] = left[leftIndex]
            leftIndex += 1
            index += 1

        while rightIndex < len(right):
            array[index] = right[rightIndex]
            rightIndex += 1
            index += 1
            # this is a comment


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
