# Given 2 arrays, create a function that let's a user know(true/false) whether these two arrays contain any common items

# array1 = ["a", "b", "c", "x"]
# array2 = ["z", "y", "i"]
# should return False

array1 = ["a", "b", "c", "x"]
array2 = ["z", "y", "x"]
# Shoud return True


# def findingCommon(array1, array2):  # first approach brute force, Time Complexity = O(n*m)
#     for item1 in array1:
#         for item2 in array2:
#             if item1 == item2:
#                 return True
#     return False


# print(findingCommon(array1, array2))


# use hash table aka dictionary in python

def containsCommonItem(array1, array2):  # Time Complexity = O(n+m)
    map = {}
    for i in array1:
        map[i] = True
    for j in array2:
        if map.get(j) == True:
            return True
    return False


print(containsCommonItem(array1, array2))
