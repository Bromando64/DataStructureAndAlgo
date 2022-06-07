# Google Question
# Given an Array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an Array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an Array = [2,3,4,6]:
# It should return False

arr = [2, 1, 1, 2, 3, 5, 1, 2, 4]


def firstRecurringChar(arr):  # O(n)
    map = {}
    for i in arr:
        if map.get(i) == True:
            return i
        map[i] = True
    return False


print(firstRecurringChar(arr))


# def firstRecurringChar(arr):  # O(n^2)
#     newarr = []
#     for i in arr:
#         if i in newarr:
#             return i
#         newarr.append(i)
#     return False


# print(firstRecurringChar(arr))
