class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem

    def delete(self, index):
        self.shiftItemsLeft(index)
        del self.data[self.length - 1]
        self.length -= 1

    def replace(self, data,  index):
        self.data[index] = data

    def insert(self, data, index):
        self.shiftItemsRight(index)
        self.replace(data, index)

    def shiftItemsLeft(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]

    def shiftItemsRight(self, index):
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]


newArray = MyArray()

newArray.push("hi")
newArray.push("you")
newArray.push("!")
newArray.push("hell")
newArray.push("ball")
newArray.push("doll")
newArray.push("call")
newArray.insert("lmao", 1)
print(newArray.data)
