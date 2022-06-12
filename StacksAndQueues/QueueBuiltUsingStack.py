# O(n) time complexity for push

# class MyQueue:

#     def __init__(self):
#         self.s1 = []
#         self.s2 = []

#     def push(self, x: int) -> None:
#         while self.s1:
#             self.s2.append(self.s1.pop())
#         self.s1.append(x)
#         while self.s2:
#             self.s1.append(self.s2.pop())

#     def pop(self) -> int:
#         return self.s1.pop()

#     def peek(self) -> int:
#         return self.s1[-1]

#     def empty(self) -> bool:
#         return not self.s1


# O(1) time complexity for pop in average
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
