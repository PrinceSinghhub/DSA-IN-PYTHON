class BST:

    def __init__(self,root,left,right):
        self.R=root
        self.Lchlid=left
        self.Rchlid=right
    def bst_print(self):
        print(self.R)
        print(self.Lchlid)
        print(self.Rchlid)

cls = BST(20,None,None)
cls.bst_print()
print()
cls1 = BST(200,10,None)
cls1.bst_print()
print()

