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
        pass

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass


myQueue = Queue()
