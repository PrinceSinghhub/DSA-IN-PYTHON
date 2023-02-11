import heapq
class MinHeap:
    def __init__(self):
        self.heap = []

    def insertation(self,element):
        heapq.heappush(self.heap,element)
        # root.insertation()

    def printData1(self):
        return self.heap

    def remove(self):
        print(heapq.heappop(self.heap))

    # todo after detelet the node
    def printData2(self):
        return self.heap

    # todo convert list in to binary heap
    def heapify(self,List):
        heapq.heapify(List)
        return List

    # todo deletion and insertion both in one time
    def pushpop(self,element):
        print(heapq.heappushpop(self.heap,element))

    def printData3(self):
        return self.heap

    # todo remove element and insert element

    def heapreplace(self,element):
        print(heapq.heapreplace(self.heap,element))


    def printData4(self):
        return self.heap

    # todo find the minimum element in heap
    def MinElement(self,arr,n):
        print(heapq.nsmallest(n,arr))

    # todo find the maximum element in heap
    def MaxElement(self,arr,n):
        print(heapq.nlargest(n,arr))




root = MinHeap()

arr = [5,10,1,11,2,15,-1]
for i in arr:
    root.insertation(i)

print(root.printData1())
root.remove()

print(root.printData2())

List = [5,1,3,-2,4,11,6]
print(root.heapify(List))

root.pushpop(100)
print(root.printData3())

root.heapreplace(202)
print(root.printData4())

arr = [5,4,7,8,9,1,2,10]
root.MinElement(arr,2)

root.MaxElement(arr,3)