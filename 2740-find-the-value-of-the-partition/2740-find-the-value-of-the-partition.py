import sys

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse =True)
        num_min = sys.maxsize
        
        for i in range(len(nums)-1):
            diff = nums[i] - nums[i+1]
            num_min  = min(diff, num_min)
        
        return num_min