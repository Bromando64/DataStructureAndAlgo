class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.last == None:
            return None
        return self.first.value

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.last == None:
            return None
        if self.last == self.first:
            self.first == None
        self.first = self.first.next
        self.length -= 1


myQueue = Queue()
myQueue.enqueue("Yalung")
myQueue.enqueue("Sahil")
myQueue.enqueue("Nishant")
myQueue.enqueue("Ronan")
myQueue.dequeue()
print(myQueue.peek())
