class BST:
    def __init__(self, data):
        self.root = data
        self.Lchild = None
        self.Rchild = None

    # todo insertation data

    def insertion(self, node):
        if self.root == None:
            self.root = node

        if self.root == node:
            pass

        if self.root > node:
            if self.Lchild == None:
                self.Lchild = BST(node)

            else:
                self.Lchild.insertion(node)

        if self.root < node:
            if self.Rchild == None:
                self.Rchild = BST(node)

            else:
                self.Rchild.insertion(node)



    # Function to  print level order traversal of tree
    def printLevelOrder(self,root):
        h = self.height(root)
        for i in range(1, h + 1):
            self.printCurrentLevel(root, i)

    # Print nodes at a current level
    def printCurrentLevel(self,root, level):
        if root is None:
            return
        if level == 1:
            print(root.root, end=" ")
        elif level > 1:
            self.printCurrentLevel(root.Lchild, level - 1)
            self.printCurrentLevel(root.Rchild, level - 1)

    # compute hight of tree
    def height(self,node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.Lchild)
            rheight = self.height(node.Rchild)

            # Use the larger one
            if lheight > rheight:
                print(lheight+1)
                return lheight + 1
            else:
                print(rheight+1)
                return rheight + 1




root = BST(9)
data = [4,6,9,7,5,6,10]
for i in data:
    root.insertion(i)



print("Level order traversal in BST")
root.printLevelOrder(root)



