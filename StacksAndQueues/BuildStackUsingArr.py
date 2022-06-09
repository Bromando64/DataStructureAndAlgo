class Stack:
    def __init__(self) -> None:
        self.arr = []

    def peek(self):
        return self.arr[len(self.arr)-1]

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        self.arr.pop()


myStack = Stack()
myStack.push("Google")
myStack.push("Amazon")
myStack.push("Facebook")
myStack.push("Discord")
print(myStack.peek())
# arrays act like stacks so we can just use it regularly
