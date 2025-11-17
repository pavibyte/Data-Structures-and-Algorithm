class Solution(object):
    def maxArea(self, height):
        left = 0
        right =len(height)-1
        max_area = 0
        while(left<right):
            width = right - left
            curr_height = min(height[left],height[right])
            curr_area = width * curr_height
            max_area = max(max_area,curr_area)

            if height[left] < height[right]:
                left = left+1
            else:
                right = right-1
        return max_area
            