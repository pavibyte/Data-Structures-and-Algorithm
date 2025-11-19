class Solution:
    def leftElement(self,arr) -> int:
        # code here
        if len(arr) == 1:
            return arr[0]
        arr.sort()
        return arr[(len(arr)-1)//2]
