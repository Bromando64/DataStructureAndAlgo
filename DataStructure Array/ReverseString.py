# reverse a string using array

input = "My name is Nishant"


def reverseString(input):
    rev = ""
    for i in input:
        rev = i + rev
    print(rev)


reverseString(input)
