class node:
    def __init__(self,data):
        self.left=None
        self.Right=None
        self.centre=data

    def tree_value(self,x,y):
        a=self.left=x
        b=self.Right=y
        c=self.centre
        print(f"Basic Binary Tree Representation\n{a} {c} {b}")
        print()
        print(f"{c} is Root Node\n{a} and {b} is a Child Node of Root Node")

X=node(20)
X.tree_value(1,2)