class BST:
    def __init__(self,root):
        self.root = root
        self.Lchild = None
        self.Rchild = None

    def insertion(self,data):
        if self.root == None:
            self.root = data

        if self.root == data:
            pass

        if self.root>data:
            if self.Lchild:
                self.Lchild.insertion(data)
            else:
                self.Lchild = BST(data)

        if self.root<data:
            if self.Rchild:
                self.Rchild.insertion(data)

            else:
                self.Rchild = BST(data)

       # todo in order traversal

    def in_order_traversal(self):

        if self.Lchild != None:
            self.Lchild.in_order_traversal()

        print(self.root, end=" ")

        if self.Rchild != None:
            self.Rchild.in_order_traversal()


    def print_tree(self):

        if self.Lchild != None:
            self.Lchild.print_tree()
        print(self.root,end=" ")
        if self.Rchild != None:
            self.Rchild.print_tree()




root=BST(60)
data = [30,100,90,200,50,55,40,30,45]
for i in data:
    root.insertion(i)
print("BST TREE")
root.print_tree()
print()
print("In Order Treversal")
root.in_order_traversal()