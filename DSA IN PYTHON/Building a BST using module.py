from binarytree import *
"""Syntax: binarytree.bst(height=3, is_perfect=False)
Parameters: 
height: It is the height of the tree and its value can be between the range 0-9 (inclusive) 
is_perfect: If set True a perfect binary is created.
Returns: Root node of the BST. """

root = bst()
print('BST of any height :',root)

root1 = bst(height=3,is_perfect=True)
print('Perfect BST of given height :',root1) 