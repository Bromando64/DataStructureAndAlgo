class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        newNode = BinaryTreeNode(value)
        if self.root == None:
            self.root = newNode
        else:
            concurentNode = self.root
            while True:
                if value < concurentNode.value:
                    # left
                    if not concurentNode.left:
                        concurentNode.left = newNode
                        return self
                    concurentNode = concurentNode.left
                else:
                    # right
                    if not concurentNode.right:
                        concurentNode.right = newNode
                        return self
                    concurentNode = concurentNode.right

    def lookup(self, value):
        if self.root == None:
            return None
        else:
            concurentNode = self.root
            while True:
                if concurentNode == None:
                    return None
                if value < concurentNode.value:
                    # left
                    concurentNode = concurentNode.left
                elif value > concurentNode.value:
                    # right
                    concurentNode = concurentNode.right
                else:
                    return concurentNode

    def remove(self, value):
        if self.root == None:
            return None
        currentNode = self.root
        parentNode = None
        while currentNode:
            if value < currentNode.value:  # move to the left
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:  # move to the right
                parentNode = currentNode
                currentNode = currentNode.right
            elif currentNode == value:
                # its a match
                # Option 1: No right Child:
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        # if parent > current value, make the current left child a child of parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        # if parent < current value, make left child a right child of the parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.left
                # Option 2: Right child which doesn't have a left child
                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if parentNode == None:
                        self.root = currentNode.right
                    else:
                        # if parent > current, make right child of the left the parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right
                        # if parent < current, make right child a right child of the parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right
                # Option 3: Right child that has a left child
                else:
                    # find the right child's left most child
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left is not None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    # Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        # if parent > current, make leftmost a left child of the parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                        # if parent < current, make leftmost a right child of the parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
                    return True

    def DFSInorder(self):
        return traverseInOrder(self.root, [])

    def DFSPostorder(self):
        return traversePostOrder(self.root, [])

    def DFSPreorder(self):
        return traversePreOrder(self.root, [])


def traverseInOrder(node, list):
    if node.left:
        traverseInOrder(node.left, list)
    list.append(node.value)
    if node.right:
        traverseInOrder(node.right, list)
    return list


def traversePreOrder(node, list):
    list.append(node.value)
    if node.left:
        traversePreOrder(node.left, list)
    if node.right:
        traversePreOrder(node.right, list)
    return list


def traversePostOrder(node, list):
    if node.left:
        traversePostOrder(node.left, list)
    if node.right:
        traversePostOrder(node.right, list)
    list.append(node.value)
    return list


binarySearch = BinarySearchTree()
binarySearch.insert(9)
binarySearch.insert(4)
binarySearch.insert(6)
binarySearch.insert(20)
binarySearch.insert(170)
binarySearch.insert(15)
binarySearch.insert(1)

print(binarySearch.DFSInorder())
print(binarySearch.DFSPreorder())
print(binarySearch.DFSPostorder())

#         9
#     4       20
# 1     6  15    170
