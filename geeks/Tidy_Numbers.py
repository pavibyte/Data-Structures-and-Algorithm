class Solution:
    def isTidy(self,N):
        #code here
        num = str(N)
        for i in range(len(num)-1):
            if (int(num[i]) > int(num[i+1]) ):
                return 0
        return 1