class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for k in words:
            i = list(k)
            if len(i) == len(pattern) and len(set(i)) == len(set(pattern)) and len(set(zip(i,pattern))) == len(set(i)):
                result.append(k)
        return result
            
            
        