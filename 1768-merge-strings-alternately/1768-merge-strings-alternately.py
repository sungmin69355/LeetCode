class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r1 = list(word1)
        r2 = list(word2)
        result = list()
        cnt = max(len(r1), len(r2))
        
        for i in range(cnt):
            if len(r1) > i:
                result.append(r1[i])
            if len(r2) > i:
                result.append(r2[i])
            
        return ''.join(result)
        