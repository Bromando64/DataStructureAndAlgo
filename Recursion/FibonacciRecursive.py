# given a number N return the index value of the fibonacci sequence, where the sequnce is:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...


def iterative(number):
    # a = 0
    # b = 1
    # for i in range(number):
    #     c = a + b
    #     a = b
    #     b = c
    # print(a)
    arr = [0, 1]
    for i in range(2, number+1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[number]


print(iterative(3))


def recursive(number):
    if number < 2:
        return number
    return recursive(number - 1) + recursive(number - 2)


print(recursive(8))
