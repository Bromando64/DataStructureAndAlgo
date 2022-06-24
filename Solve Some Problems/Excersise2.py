# an array of numbers and find a matching pair that is equal to the sum given

# Eg
# [1,2,3,4] Sum = 8  No
# [1,2,4,4] Sum = 8  Yes


arr = [1, 2, 4, 4]
# arr = [1, 2, 3, 4]
sum = 8


# when sorted

# Naive Approach
def findTheSumOfPair(arr):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                return True
    return False


# print(findTheSumOfPair(arr))


# Better Approach for sorted array
def findTheSumOfPair2(arr):
    low = 0
    hi = len(arr)-1
    while low < hi:
        s = arr[low] + arr[hi]
        if s == sum:
            return True
        elif s < sum:
            low += 1
        elif s > sum:
            hi -= 1
        if hi == low:
            return


# print(findTheSumOfPair2(arr))


# unsorted

def findTheSumOfPair3(arr):
    map = set()
    for i in range(len(arr)):
        comp = abs(sum - arr[i])
        if comp in map:
            return True
        map.add(arr[i])
    return False


print(findTheSumOfPair3(arr))
