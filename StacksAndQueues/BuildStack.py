class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top == None:
            return None
        return self.top.value

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            temp = self.top
            self.top = newNode
            self.top.next = temp
        self.length += 1

    def pop(self):
        if self.top == None:
            return None
        if self.top == self.bottom:
            self.bottom = None
        self.top = self.top.next
        self.length -= 1


myStack = Stack()
myStack.push("Google")
myStack.push("Amazon")
myStack.push("Facebook")
myStack.push("Discord")
myStack.pop()
print(myStack.peek())
