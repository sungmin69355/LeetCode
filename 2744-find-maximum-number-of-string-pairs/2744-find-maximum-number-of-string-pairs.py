class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        result = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i][::-1] == words[j]:
                    result+=1
        
        return result
                    