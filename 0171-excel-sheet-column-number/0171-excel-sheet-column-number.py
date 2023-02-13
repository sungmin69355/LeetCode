class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        a, b = 0, 0
        for i in reversed(columnTitle):
            temp =  ord(i) - 64
            a += temp * 26**b
            b += 1
        
        return a