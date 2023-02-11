class KadanesAlgorithm:

    def use_arrayFunction(self,arr):

        # todo here we use a array function and return ans
        return max(arr)

    def MaxSum_SunArray(self,arr):

        # todo here we apply KadanesAlgorithm
        maxsum = float('-inf')

        for i in range(len(arr)):
            if arr[i]>maxsum:
                maxsum = arr[i]
        return maxsum



ans = KadanesAlgorithm()
arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print(ans.MaxSum_SunArray(arr))
print(ans.use_arrayFunction(arr))

