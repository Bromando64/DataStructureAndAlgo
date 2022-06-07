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
        self.newNode = Node(value)
        self.head = self.newNode
        self.tail = self.newNode
        self.length = 1

    def append(self, value):
        self.newNode = Node(value)
        self.tail.next = self.newNode
        self.tail = self.newNode
        self.length += 1

    def prepend(self, value):
        self.newNode = Node(value)
        self.newNode.next = self.head
        self.head = self.newNode
        self.length += 1

    def insert(self, index, value):
        self.newNode = Node(value)
        mover = self.head
        n = 1
        while n < index:
            mover = mover.next
            n += 1
        self.temp = mover.next
        mover.next = self.newNode
        self.newNode.next = self.temp
        self.length += 1

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
myLinkedList.printer()
