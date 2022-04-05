class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) >= 3:
            max_result = list(set(nums))
            max_result.sort()
            max_result.reverse()
            if len(max_result) <= 2:
                return max(max_result)
            return max_result[2]
        else:
            return max(nums)