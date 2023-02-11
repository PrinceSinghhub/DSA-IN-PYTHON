class full_BT:

    def __init__(self,root,value):
        self.R=root
        self.V=value

    def BT_values(self):
        BT = []
        BT.append(self.R)
        for i in range(self.V):
            n=int(input("Enter Values: "))
            BT.append(n)

        return BT
    def check(self):
        r=self.BT_values()

        r1=len(r)

        if r1%2!=0:
            print(f'Yes This Tree is Full BT: {r}')
        else:
            print(f'No This Tree is Not Full BT: {r}')
n=int(input("Enter Root: "))
n1=int(input("Enter Root value: "))
n=full_BT(n,n1)
n.check()

