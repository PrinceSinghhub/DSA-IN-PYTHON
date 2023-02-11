class KadanesAlgorithm:

    def use_arrayFunction(self,arr):

        # todo here we use a array function and return ans
        return sum(arr)

    def MaxSum_SunArray(self,arr):

        # todo here we apply KadanesAlgorithm
        maxsum = 0
        currentSum = 0
        for i in range(len(arr)):
            currentSum+=arr[i]
            if currentSum > maxsum:
                maxsum = currentSum
        return maxsum



ans = KadanesAlgorithm()
arr = [1,2,3,4,5,6,7,8,9,10]
print(ans.MaxSum_SunArray(arr))
print(ans.use_arrayFunction(arr))

