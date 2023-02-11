class KadanesAlgorithm:

    def MaxSum_SunArray(self,arr):

        maxsum = 0
        currentsum = 0

        for i in range(len(arr)):

            currentsum+=arr[i]
            if currentsum > maxsum:
                maxsum = currentsum

            if currentsum < 0:
                currentsum = 0

        return maxsum

ans = KadanesAlgorithm()
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(ans.MaxSum_SunArray(arr))