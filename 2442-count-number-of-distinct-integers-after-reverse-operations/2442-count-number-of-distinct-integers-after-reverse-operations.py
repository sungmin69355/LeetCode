class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:       
        result = nums
        reverse_list = []
        for i in range(len(result)):
            p = str(result[i])
            reverse_list.append(int(p[::-1]))
            
        result = nums + reverse_list
        
        return len(set(result))
        
            
            