class BST:
    def __init__(self, data):
        self.root = data
        self.Lchild = None
        self.Rchild = None

    def insertion(self, node):
        if self.root == None:
            self.root = node

        if self.root == node:
            pass

        if self.root > node:
            if self.Lchild != None:
                self.Lchild.insertion(node)

            else:
                self.Lchild = BST(node)

        if self.root < node:
            if self.Rchild != None:
                self.Rchild.insertion(node)

            else:
                self.Rchild = BST(node)

    def print_tree(self):

        if self.Lchild != None:
            self.Lchild.print_tree()
        print(self.root,end=" ")
        if self.Rchild != None:
            self.Rchild.print_tree()

    # todo max and min in BST

    def find_max(self):
        if self.Rchild is None:
            print(self.root)
        return self.Rchild.find_max()

    def find_min(self):
        if self.Lchild is None:
            print(self.root)
        return self.Lchild.find_min()


r = BST(300)
data = [50,100,40,55,90,200,30,45]
for i in data:
    r.insertion(i)
r.print_tree()
r.find_min()
r.find_max()