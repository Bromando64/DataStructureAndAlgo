def recursiveFact(number):
    if number == 2:
        return 2
    return number * recursiveFact(number - 1)


print(recursiveFact(5))
