class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        def isPrime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0: return False
            return True
        
        list_num = []
        result = []
        for i in range(len(nums)):
            list_num.append(nums[i][i])
        
        max_nums = len(nums[0])-1
        for i in range(0, len(nums)):
            list_num.append(nums[i][max_nums])
            max_nums -= 1
        
        for i in range(len(list_num)):
            if isPrime(list_num[i]):
                 result.append(list_num[i])
        
        if len(result) > 0:
            if max(result) == 1:
                return 0
            return max(result)
        return 0