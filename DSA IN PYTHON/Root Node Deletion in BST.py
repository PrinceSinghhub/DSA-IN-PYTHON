# todo this programe is only work for main root node only
class BST:
    def __init__(self, data):
        self.root = data
        self.Lchild = None
        self.Rchild = None

    def insertion(self,data):
        if self.root == None:
            self.root = data

        if self.root == data:
            pass

        if self.root>data:
            if self.Lchild:
                self.Lchild.insertion(data)
            else:
                self.Lchild = BST(data)

        if self.root<data:
            if self.Rchild:
                self.Rchild.insertion(data)

            else:
                self.Rchild = BST(data)


    def print_tree(self):

        if self.Lchild != None:
            self.Lchild.print_tree()
        print(self.root, end=" ")
        if self.Rchild != None:
            self.Rchild.print_tree()

    # todo deletation
    def delete(self, node,current): #current = root.node
        # if root is empty
        if self.root == None:
            print("Tree is Empty")
            return

        # search leftnode and rightnode in BST
        if self.root > node:
            if self.Lchild: #self.Lchild!=None
                self.Lchild = self.Lchild.delete(node,current)
            else:
                print("Given Node not Present in BST")

        elif self.root<node:
            if self.Rchild: #self.Rchild!=None
                self.Rchild = self.Rchild.delete(node,current)
            else:
                print("Given Node not Present in BST")

        # if deleted node is root node
        else:
            # todo only 1 child node contains then this condition apply
            # if Lchild is none then return rchild
            if self.Lchild is None:
                temp = self.Rchild

                if node == current:
                    self.root = temp.root
                    self.Lchild = temp.Lchild
                    self.Rchild = temp.Rchild
                    temp = None
                    return
                self = None
                return temp

            # if Rchild is none then return Lchild
            if self.Rchild is None:
                temp = self.Lchild

                if node == current:
                    self.root = temp.root
                    self.Lchild = temp.Lchild
                    self.Rchild = temp.Rchild
                    temp = None
                    return

                self = None
                return temp

            # todo 2 chlid node contains then this condition apply
            # first we want to find smallest node in right subtee
            node = self.Rchild
            while node.Lchild: #also write node.Lchild!=None
                node = node.Lchild

            self.root = node.root
            self.Rchild = self.Rchild.delete(node.root,current)

        return self




def count(node):

    if node is None:
        return 0

    return 1+count(node.Lchild)+count(node.Rchild)



ans=BST(10)
data1 = [1,12]
for i in data1:
    ans.insertion(i)
print(count(ans))

if count(ans)>1:
    ans.delete(120,ans.root)

else:
    print("soory we not able to performe deletatoin in BST")

ans.print_tree()

