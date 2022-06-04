class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
            
        
        def s_rob(nums, i, j):
            rob_a, rob_b = 0,0 
            for idx in range(i,j):
                num = nums[idx]
                rob_a, rob_b = rob_b + num, max(rob_a, rob_b)    
            return max(rob_a, rob_b)
        
        n = len(nums)
        return max(s_rob(nums, 1, n), s_rob(nums, 0, n-1))