
class Solution:
  
    def rotateArr(self, arr, d):
        
        n = len(arr)
        d = d%n
        
        temp = arr[:d]
        arr[:n-d] = arr[d:]
        arr[n-d:] = temp
        
        return arr