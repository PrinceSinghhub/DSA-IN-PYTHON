'''Syntax: binarytree.build(values)
Parameters:
values: List representation of the binary tree.
Returns: root of the binary tree. '''
from binarytree import*
nodes=[6,5,3,4,2,1,0]
binary_tree=build(nodes)
print(f"binary tree: {binary_tree}")

binary_tree1 = binary_tree.values
print(f"binary tree list: {binary_tree1}")

binary_tree2 = binary_tree.left
print(f"binary left tree: {binary_tree2}")

binary_tree2 = binary_tree.right
print(f"binary right tree : {binary_tree2}")

binary_tree2 = binary_tree.leaves
print(f"binary leaves tree : {binary_tree2}")

binary_tree2 = binary_tree.levels
print(f"binary levels tree : {binary_tree2}")

binary_tree2 = binary_tree.height
print(f"binary height tree : {binary_tree2}")

# todo get full properties
print('Properties of tree : \n', binary_tree.properties)