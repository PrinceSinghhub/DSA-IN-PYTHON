import heapq
class PriovertyQueue:
    def __init__(self,array):
        self.heap = array

    def heapify(self):
        heapq.heapify(self.heap)

    def excessData(self):
        for i in range(len(self.heap)):
            print(heapq.heappop(self.heap))

arr = [(3,"codex coder"),(1,"CODER"),(2,"CODEX")]
root = PriovertyQueue(arr)
root.heapify()
root.excessData()
