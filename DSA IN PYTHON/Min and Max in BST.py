class BST:
    def __init__(self,data):
        self.root = data
        self.Lchild = None
        self.Rchild = None


    def insertation(self,node):

        if self.root == None:
            self.root = node

        if self.root == node:
            pass

        if self.root>node:
            if self.Lchild:
                self.Lchild.insertation(node)

            else:
                self.Lchild = BST(node)

        if self.root<node:
            if self.Rchild:
                self.Rchild.insertation(node)

            else:
                self.Rchild = BST(node)

    def printTree(self):
        if self.Lchild!=None:
            self.Lchild.printTree()
        print(self.root,end = " ")

        if self.Rchild!=None:
            self.Rchild.printTree()

    # todo find Min and Max

    def minNode(self):

        current_node = self
        while current_node.Lchild!=None:
            current_node = current_node.Lchild

        print(f"the Min Node is: {current_node.root}")

    def maxNode(self):
        current_node = self
        while current_node.Rchild!=None:
            current_node = current_node.Rchild

        print(f"the Max Node is: {current_node.root}")

ans = BST(10)
arr = [2,110,3,18,-1]
for i in arr:
    ans.insertation(i)
ans.printTree()
print()
ans.minNode()
ans.maxNode()