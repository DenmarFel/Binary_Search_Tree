import collections

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # This is a sorted binary tree
    def __init__(self, value: int):
        self.root = Node(value)

    def add(self, value: int):
        '''Adds a value(Node) into the BST'''
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(self.root, value)
    
    def _add(self, root: Node, value):
        ''' Helper function for add.'''
        if value < root.value:
            if root.left:
                self._add(root.left, value)
            else:
                root.left = Node(value)
        elif value > root.value:
            if root.right:
                self._add(root.right, value)
            else:
                root.right = Node(value)
        else:
            print("Sorry!", str(value), "already exists in the tree!")
    
    def getOrder(self, type: str):
        if type == 'preorder':
            return self._preorder(self.root)
        elif type == 'inorder':
            return self._inorder(self.root)
        elif type == 'postorder':
            return self._postorder(self.root)
        elif type == 'level-order':
            return self._levelOrder(self.root)
        else:
            'Sorry! Please specify an order type.'

    def _preorder(self, root: Node):
        '''A pre-order (DFS) traversal for a binary tree'''
        values = []
        if root:
            values.append(root.value)
            values.extend(self._preorder(root.left))
            values.extend(self._preorder(root.right))
        return values
    
    def _inorder(self, root: Node):
        '''A in-order (DFS) traversal for a binary tree'''
        values = []
        if root:
            values.extend(self._inorder(root.left))
            values.append(root.value)
            values.extend(self._inorder(root.right))
        return values
    
    def _postorder(self, root: Node):
        '''A post-order (DFS) traversal for a binary tree'''
        values = []
        if root:
            values.extend(self._postorder(root.left))
            values.extend(self._postorder(root.right))
            values.append(root.value)
        return values

    def _levelOrder(self, root: Node):
        '''A level-order (BFS) traversal for a binary tree'''
        values = []
        queqe = collections.deque([])
        current = root
        while current:
            values.append(current.value)
            queqe.append(current.left)
            queqe.append(current.right)
            current = queqe.popleft()
        return values

    def getMaxDepth(self):
        return self._getMaxDepth(self.root)

    def _getMaxDepth(self, root: Node):
        if root == None:
            return 0
        else:
            return max(self._getMaxDepth(root.left), self._getMaxDepth(root.right)) + 1
            

    

            
a = BinarySearchTree(5)
a.add(3)
a.add(2)
a.add(4)
a.add(7)
a.add(6)
a.add(9)

'''
                5
        /               \
        3                7
    /       \        /       \
    2       4        6       9
'''
print(a.getOrder('preorder'))
print(a.getOrder('inorder'))
print(a.getOrder('postorder'))
print(a.getOrder('level-order'))
print(a.getOrder('order'))
print(a.getMaxDepth())