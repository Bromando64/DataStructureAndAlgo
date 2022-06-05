#mergeSorted [0,3,4,31], [4,6,30]


arr1 = [0, 3, 4, 31, 43, 45, 90]
arr2 = [4, 6, 30, 35, 40, 42, 43]


def mergeSortedArr(arr1, arr2):
    newArr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            newArr.append(arr1[i])
            i += 1
        else:
            newArr.append(arr2[j])
            j += 1
    while i < len(arr1):
        newArr.append(arr1[i])
        i += 1
    while j < len(arr2):
        newArr.append(arr2[j])
        j += 1
    return newArr


print(mergeSortedArr(arr1, arr2))


# for i in arr1:
#     newArr.append(i)
# for j in arr2:
#     newArr.append(j)
# newArr.sort()
