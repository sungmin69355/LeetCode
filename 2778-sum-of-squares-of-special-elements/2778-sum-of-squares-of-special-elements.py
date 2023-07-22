class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        nums_len = len(nums)
        for i in range(len(nums)):
            if nums_len % (i+1) == 0:
                result += nums[i] * nums[i] 
        return result