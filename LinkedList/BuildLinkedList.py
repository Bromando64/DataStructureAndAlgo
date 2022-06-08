# myLinkedlist = {
#     "head": {
#         "value": 10,
#         "next": {
#             "value": 5,
#             "next": {
#                 "value": 16,
#                 "next": None
#             }
#         }
#     }
# }

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self, index, value):
        # check the parameter
        if index >= self.length:
            return self.append(value)
        newNode = Node(value)
        mover = self.traversal(index - 1)
        temp = mover.next
        mover.next = newNode
        newNode.next = temp
        self.length += 1

    def delete(self, index):
        if index >= self.length:
            return "err"
        mover = self.traversal(index - 1)
        temp = mover.next
        mover.next = temp.next
        self.length -= 1

    def traversal(self, index):
        mover = self.head
        n = 0
        while n < index:
            mover = mover.next
            n += 1
        return mover

    def printer(self):
        temp = self.head
        arr = []
        while temp:
            arr.append(temp.value)
            temp = temp.next
        print(arr)


myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(25)
myLinkedList.append(16)
myLinkedList.prepend(12)
myLinkedList.insert(2, 99)
myLinkedList.delete(3)
myLinkedList.printer()
