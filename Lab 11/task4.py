class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)
    def _insert_recursive(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        return node
    def search(self, target):
        return self._search_recursive(self.root, target)
    def _search_recursive(self, node, target):
        if node is None:
            return False
        if target == node.data:
            return True
        if target < node.data:
            return self._search_recursive(node.left, target)
        return self._search_recursive(node.right, target)
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)
print("Inorder Traversal:", bst.inorder_traversal())
print("Search 60:", bst.search(60))
print("Search 25:", bst.search(25))