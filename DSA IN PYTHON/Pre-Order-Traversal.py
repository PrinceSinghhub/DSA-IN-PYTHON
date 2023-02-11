class BST:
    def __init__(self,value):
        self.root = value
        self.lchild = None
        self.rchild = None

    def insertion(self,node):
        if self.root == None:
            self.root = node

        if self.root == node:
            pass

        if self.root>node:
            if self.lchild == None:
                self.lchild = BST(node)
            else:
                self.lchild.insertion(node)
        if self.root < node:
            if self.rchild == None:
                self.rchild = BST(node)
            else:
                self.rchild.insertion(node)

    def print_tree(self):
        if self.lchild != None:
            self.lchild.print_tree()
        print(self.root,end=" ")
        if self.rchild != None:
            self.rchild.print_tree()

    # todo pre-order
    def pre_order(self):
        print(self.root,end = " ")
        if self.lchild != None:
            self.lchild.pre_order()

        if self.rchild != None:
            self.rchild.pre_order()


root=BST(10)
data = [6,3,1,6,98,3,7]
for i in data:
    root.insertion(i)
root.print_tree()
print()
print("Pre-Order")
root.pre_order()