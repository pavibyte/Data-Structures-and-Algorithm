class Solution:
    def findSingle(self, arr):
        new_list = []
        for i in arr:
            if i in new_list:
                new_list.remove(i)
            else:
                new_list.append(i)
                
        return new_list[0]