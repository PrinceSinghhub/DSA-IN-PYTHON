class BST:

    def __init__(self,data):
        self.root= data
        self.Lchild = None
        self.Rchild = None

    def insert(self,node):

        if self.root == None:
            self.root = node

        if self.root == node:
            pass

        if self.root>node:
            if self.Lchild != None:
                self.Lchild.insert(node)

            else:
                self.Lchild = BST(node)

        if self.root<node:
            if self.Rchild != None:
                self.Rchild.insert(node)

            else:
                self.Rchild = BST(node)

    def tree(self):

        if self.Lchild != None:
            self.Lchild.tree()

        print(self.root,end=" ")

        if self.Rchild != None:
            self.Rchild.tree()

    # todo in post order traversal

    def post_order_traversal(self):

        if self.Lchild != None:
            self.Lchild.post_order_traversal()

        if self.Rchild != None:
            self.Rchild.post_order_traversal()

        print(self.root, end=" ")

root = BST(60)
data = [50,100,40,55,90,200,30,45]
for i in data:
    root.insert(i)
print("BST TREE")
root.tree()
print()
print("POST-ORDER")
root.post_order_traversal()
