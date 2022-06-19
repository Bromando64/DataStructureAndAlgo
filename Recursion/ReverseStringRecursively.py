
input = "My name is Nishant"


def reverseString(input):
    rev = ""
    for i in input:
        rev = i + rev
    print(rev)


reverseString(input)


def reverseStringRecursive(input):
    if len(input) == 1:
        return input
    return reverseStringRecursive(input[1:]) + input[0]


print(reverseStringRecursive(input))
