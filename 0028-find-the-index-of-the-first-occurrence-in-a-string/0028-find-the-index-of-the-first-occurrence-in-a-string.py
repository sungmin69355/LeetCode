class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        if len(needle) == len(haystack) and needle == haystack:
            return 0
        
        size_needle = len(needle)
        for i in range(0, len(haystack)):
            if haystack[i:size_needle+i] == needle:
                return i
        return -1