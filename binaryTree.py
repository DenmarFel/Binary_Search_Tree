class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
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

    def _preorder(self, root):
        values = []
        if root:
            values.append(root.value)
            values.extend(self._preorder(root.left))
            values.extend(self._preorder(root.right))
        return values
    
    def _inorder(self, root):
        values = []
        if root:
            values.extend(self._inorder(root.left))
            values.append(root.value)
            values.extend(self._inorder(root.right))
        return values
    
    def _postorder(self, root):
        values = []
        if root:
            values.extend(self._postorder(root.left))
            values.extend(self._postorder(root.right))
            values.append(root.value)
        return values
        
    def getOrder(self, type):
        if type == 'preorder':
            return self._preorder(self.root)
        elif type == 'inorder':
            return self._inorder(self.root)
        elif type == 'postorder':
            return self._postorder(self.root)
        else:
            'Sorry! Please specify an order type.'

            
a = BinaryTree(5)
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
print(a.getOrder('order'))