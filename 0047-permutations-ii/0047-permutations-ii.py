from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        combi = list(set(permutations(nums, len(nums))))
        
        return combi