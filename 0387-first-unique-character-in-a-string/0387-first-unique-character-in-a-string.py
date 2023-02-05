class Solution:
    def firstUniqChar(self, s: str) -> int:
       
        if len(s) == 1:
            return 0
        
        letter = 'qwertyuiopasdfghjklzxcvbnm'
        result = []
        for i in letter:
            if s.count(i) == 1:
                result.append(s.index(i))
        if len(result) > 0:
            return min(result)
        return -1