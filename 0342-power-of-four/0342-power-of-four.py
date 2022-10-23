class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        for i in range(n):
            if n == (4**i):
                return True
            if n < (4**i):
                return False
                
        return False