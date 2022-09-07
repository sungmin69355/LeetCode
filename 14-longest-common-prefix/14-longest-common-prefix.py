class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
#         minstr = min(strs, key=len)
#         ret =""
#         for i in range(len(minstr)):
#             cur = strs[0][i]
#             for j in range(1,len(strs)):
#                 if strs[j][i] != cur:
#                     return ret
#             ret = ret+cur
#         return ret
        if not strs:
            return ""
        res = min(strs, key=len)
        for s in strs:
            while not s.startswith(res):
                print(res)
                res = res[0:len(res) - 1]
        return res