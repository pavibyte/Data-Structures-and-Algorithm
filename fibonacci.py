class Solution:
    #Function to return list containing first n fibonacci numbers. Iterative approach
    def fibonacciNumbers(self,n):
        arr = []
        f1 = 0
        f2 = 1
        arr.append(f1)
        for i in range(1, n):
            arr.append(f2)
            next = f1+f2
            f1 = f2
            f2 = next
        return arr