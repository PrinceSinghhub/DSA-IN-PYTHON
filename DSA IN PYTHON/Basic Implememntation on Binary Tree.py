class BST:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.root = data

    def data(self,a,b):
        BTS = []
        x=self.left = a
        y= self.right = b
        z=self.root
        # todo according to poisition in binary tree not required
        BTS.append(z);BTS.insert(0,x);BTS.insert(2,y);
        print(BTS)


c=BST(10)
c.data(None,None)
d=BST(50)
d.data(20,10)

