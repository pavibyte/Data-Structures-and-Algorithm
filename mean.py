class Solution:
    def findMean(self, arr):
        # code here 
        sum = 0
        for i in arr:
            sum += i
        return sum//len(arr)