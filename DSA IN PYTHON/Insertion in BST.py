class BST:
    def __init__(self,key):
        self.root = key
        self.Lchild = None
        self.Rchild = None

    def insertion(self,data):
        if self.root is None:
            self.root = data

        # todo dublicate data
        if self.root == data:
            pass

        # todo for lefr and right position find where we insert

        if self.root > data:
            if self.Lchild != None:   #like this if self.Lchild: = if None return false
                # todo again check data using recursion
                self.Lchild.insertion(data)

            else:
                self.Lchild = BST(data)


        else:
            if self.Rchild: #also write if self.Rchild != None

                # todo again check data using recursion
                self.Rchild.insertion(data)

            else:

                self.Rchild = BST(data)

    def PrintTree(self):
        if self.Lchild !=None:
            self.Lchild.PrintTree()
        print(self.root,end=" "),
        if self.Rchild != None:
            self.Rchild.PrintTree()


root = BST(20)
t=[50,9,6,10,46,39]
for i in t:
    root.insertion(i)
root.PrintTree()
