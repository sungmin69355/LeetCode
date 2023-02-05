class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        left, right = 0, len(nums)-1
        while (left < right and right > left):
            if nums[left] != target:
                left += 1
            if nums[right] != target:
                right -= 1
            
            if nums[left] == target and nums[right] == target:
                return [left,right]
            
        if nums[left] != target or nums[right] != target:
            return [-1,-1]
        else:
            return [left,right]