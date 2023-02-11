class BST:
    def __init__(self,key):
        self.key = key
        self.Lchild = None
        self.Rchild = None

    def print_data(self):
        print(self.key)
        print(self.Lchild)
        print(self.Rchild)

cls = BST(10)
print("TEST 1 Normal BST With 2 Node")
cls.print_data()
print()
# todo create another node
print("TEST 2 add address in Left Node")
cls.Lchild = BST(5)
print(cls.key)
# todo lchild take a address becouse creane a chlid node in Lchild
print(cls.Lchild)
print(cls.Rchild)


# todo creat Lchild new Node
print()
print("TEST 3 add subtree of left subtree")
cls.Lchild.Rchild= 9
print(cls.Lchild.key)
print(cls.Lchild.Lchild)
print(cls.Lchild.Rchild)

print()

print("TEST 4 add address in right Node")
cls.Rchild = BST(15)

print(cls.key)
# todo Rchild take a address becouse creane a chlid node in Rchild
print(cls.Lchild)
print(cls.Rchild)

print()

# todo creat Rchild new Node
print("TEST 5 add subtree of right subtree")
cls.Rchild.Lchild = 12
cls.Rchild.Rchild= 30
print(cls.Rchild.key)
print(cls.Rchild.Lchild)
print(cls.Rchild.Rchild)