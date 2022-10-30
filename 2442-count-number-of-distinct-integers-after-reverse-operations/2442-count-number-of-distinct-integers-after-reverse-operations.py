class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:       
        result = nums
        reverse_list = []
        for i in range(len(result)):
            p = str(result[i])
            reverse_list.append(int(p[::-1]))
        return len(set(nums + reverse_list))
            
            