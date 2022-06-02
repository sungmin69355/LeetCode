class Solution:
    def tribonacci(self, n: int) -> int:
        
        result = [0,1,1]
        for i in range(n):
            result.append(result[i] + result[i+1] + result[i+2])
            if len(result) > n:
                return result[n]
        
        return result[n]