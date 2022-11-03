class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def solution(n, q):
            rev_base = ''
            while n > 0:
                n, mod = divmod(n, q)
                rev_base += str(mod)
            return rev_base[::-1] 
    
        for i in range(2, n):
            temp = list(solution(n, i))
            l = len(temp) - 1
            for i in range(0, int(len(temp)/2)):
                if temp[i] != temp[l]:
                    return False
                l -= 1
    
    
        return True