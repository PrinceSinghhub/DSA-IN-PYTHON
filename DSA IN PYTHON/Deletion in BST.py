class BST:
    def __init__(self, data):
        self.root = data
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


    def print_tree(self):

        if self.Lchild != None:
            self.Lchild.print_tree()
        print(self.root, end=" ")
        if self.Rchild != None:
            self.Rchild.print_tree()

    # todo for delete node

    def delete(self, node):
        # if root is empty
        if self.root == None:
            print("Tree is Empty")
            return

        # search leftnode and rightnode in BST
        if self.root > node:
            if self.Lchild: #self.Lchild!=None
                self.Lchild = self.Lchild.delete(node)
            else:
                print("Given Node not Present in BST")

        elif self.root<node:
            if self.Rchild: #self.Rchild!=None
                self.Rchild = self.Rchild.delete(node)
            else:
                print("Given Node not Present in BST")

        # if deleted node is root node
        else:
            # todo 0 and 1 child node contains then this condition apply
            # if Lchild is none then return rchild
            if self.Lchild is None:
                temp = self.Rchild
                self = None
                return temp

            # if Rchild is none then return Lchild
            if self.Rchild is None:
                temp = self.Lchild
                self = None
                return temp

            # todo 2 chlid node contains then this condition apply
            # first we want to find smallest node in right subtee
            node = self.Rchild
            while node.Lchild: #also write node.Lchild!=None
                node = node.Lchild

            self.root = node.ans
            self.Rchild = self.Rchild.delete(node.ans)

        return self



root=BST(60)
data = [30,100,90,200,50,55,40,30,45]
for i in data:
    root.insertion(i)
print("BST TREE")
root.print_tree()
print()
root.delete(50)
root.print_tree()
