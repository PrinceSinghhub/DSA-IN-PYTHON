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


    def delete(self, node):

        if self.root == None:
            print("Sorry BST is Empty")
            return


        if node < self.root:
            if self.Lchild:
                self.Lchild = self.Lchild.delete(node)
            else:
                print("Sorry Given Node is Not Present is the Tree ")

        elif node > self.root:
            if self.Rchild:
                self.Rchild = self.Rchild.delete(node)

            else:
                print("Sorry Given Node is Not Present is the Tree ")

        else:
            if self.Lchild == None and self.Rchild == None:
                return None
            elif self.Lchild is None: #alsoe writ self.Lchild ==  None
                return self.Rchild
            elif self.Rchild is None:
                return self.Lchild

            min_val = self.Rchild.find_min()
            self.root = min_val
            self.Rchild = self.Rchild.delete(min_val)

        return self

    def find_max(self):
        if self.Rchild is None:
            return self.root
        return self.Rchild.find_max()

    def find_min(self):
        if self.Lchild is None:
            return self.root
        return self.Lchild.find_min()

r = BST(300)
data = [50,100,40,55,90,200,30,45]
for i in data:
    r.insertion(i)
print("Before Deletion")
r.print_tree()
print()
print("After Deletion")
r.delete(100)
r.print_tree()
