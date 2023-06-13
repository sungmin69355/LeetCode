class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = set()
        
        left, right = 0,len(height)-1
        
        
        if len(height) == 2:
            return min(height[left],height[right])
        
        while left != right:
            if height[left] <= height[right]:
                area.add(height[left] * (right-left))
                left+=1
            else:
                area.add(height[right] * (right-left))
                right-=1
                
        return max(area)