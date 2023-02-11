'''tree() generates a random binary tree and returns its root node.
Syntax: binarytree.tree(height=3, is_perfect=False)
Parameters:
height: It is the height of the tree and its value can be between the range 0-9 (inclusive)
is_perfect: If set True a perfect binary is created.
Returns: Root node of the binary tree. '''

from binarytree import *
class random_binary_tree:

    # todo random binary tree
    root = tree()
    print(root)

    def __init__(self,height,is_perfect):
        self.H = height
        self.P = is_perfect

    def Bt_is_given_tree(self):
        x=tree(self.H)
        print(f"Binary tree of given height: {x}")

    def Perfect_binary_tree(self):
        x=self.H
        y=self.P
        z=tree(x,y)
        print(f"Perfect binary tree of given height :{z}")



r=random_binary_tree(2,False)
r.Bt_is_given_tree()

# todo for perfect
r.H = 3
r.P = True
r.Perfect_binary_tree()

