from binarytree import *
'''Syntax: binarytree.Node(value, left=None, right=None)
Parameters: 
value: Contains the data for a node. This value must be number. 
left: Conatins the details of left node child. 
right: Contains details of the right node child. '''

# todo Getting binary tree
a=Node(3);a.left = Node(2);a.right = Node(30);a.right=Node(60)
print(f"The Binary Tree is: \n{a}")

# todo Getting list of nodes
print('List of nodes :', list(a))

# todo Getting pre-order of nodes
print('pre-order of nodes :', a.preorder)

# todo Getting post-order of nodes
print('post-order of nodes :', a.postorder)

# todo Getting inorder of nodes
print('Inorder of nodes :', a.inorder)

# todo Checking tree properties
print('Size of tree :', a.size)
print('Height of tree :', a.height)

# todo Get all properties at once
print('Properties of tree : \n', a.properties)

# todo check is BSR OR NOT
print('BST Or NOT:', a.is_bst)