class BST:
    def __init__(self,data):
        self.root = data
        self.Lchind = None
        self.Rchild = None

    # todo inserti node in BST
    def insertion(self,node):
        if self.root == None:
            self.root = node

        if self.root == node:
            pass

        if self.root > node:
            if self.Lchind == None:
                self.Lchind = BST(node)

            else:
                self.Lchind.insertion(node)

        if self.root < node:
            if self.Rchild == None:
                self.Rchild = BST(node)

            else:
                self.Rchild.insertion(node)
   # todo print bst
    def print_tree(self):
        if self.Lchind != None:
            self.Lchind.print_tree()

        print(self.root,end=" ")
        if self.Rchild != None:
            self.Rchild.print_tree()

    # todo for searcing
    def searching(self,data):
        if self.root == None:
            print(f"Sorry {data} is not Found in BST")

        if self.root == data:
            print(f"Yes {data} Found in BST")

        if self.root < data:
            if self.Rchild == None:
                print(f"Sorry {data} is not Found in BST")

            else:
                self.Rchild.searching(data)

        if self.root > data:
            if self.Lchind == None:
                print(f"Sorry {data} is not Found in BST")
            else:
                self.Lchind.searching(data)

x=BST(9)
data = [4,6,9,7,5,6,10]
for i in data:
    x.insertion(i)
print("AFTER INSERTION GIVEN BST IS")
x.print_tree()
print()
print("SEARCHING NODE ARE PRSENT OR NOT")
n=int(input("Enter Node For Search: "))
x.searching(n)