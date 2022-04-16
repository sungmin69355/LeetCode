class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        arr = Counter(nums)
        for i,j in arr.items():
            if j==1:
                return i