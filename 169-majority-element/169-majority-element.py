class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = Counter(nums)
        
        return arr.most_common()[0][0]