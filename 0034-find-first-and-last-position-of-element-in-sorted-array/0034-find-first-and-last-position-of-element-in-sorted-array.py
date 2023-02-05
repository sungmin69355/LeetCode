class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        r = len(nums)-1
        l = 0
        
        if len(nums) == 0:
            return [-1,-1]
        
        while l < r and r > l:
            if nums[l] != target:
                l+=1
            if nums[r] != target:
                r-=1
            if nums[l] == target and nums[r] == target:
                return [l,r]
            
           
        if nums[l] != target or nums[r] != target:
            return [-1,-1]
        else:
            return [l,r]