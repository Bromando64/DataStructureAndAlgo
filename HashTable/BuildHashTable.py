class HashTable:

    def __init__(self, size):
        self.data = list([""]*size)

    def set(self, key, value):
        hash = self._hash(key)

        if self.data[hash] == "":
            self.data[hash] = [key, value]
        else:
            self.data.append[[key, value]]

    def get(self, key):
        hash = self._hash(key)
        return self.data[hash][1]

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % len(self.data)
        return hash


hash = HashTable(50)
hash.set("a", 40)
print(hash.get("b"))
