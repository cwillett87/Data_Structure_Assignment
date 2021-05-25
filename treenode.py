class Treenode:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

    def insert(self, root, key):
        if root is None:
            return Treenode(key)
        else:
            if root.data == key:
                return root
            elif root.data < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def search_for_node(self, root, key):
        if root is None or root.data == key:
            if root:
                print(f'Found {root.data}')
            else:
                print('Not found!')
            return root

        if root.data < key:
            return self.search_for_node(root.right, key)

        return self.search_for_node(root.left, key)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

