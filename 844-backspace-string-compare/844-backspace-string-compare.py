class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S = []
        T = []

        for i in s:
            if i != '#':
                S.append(i)
            else:
                if S:
                    S.pop()
        
        for i in t:
            if i != '#':
                T.append(i)
            else:
                if T:
                    T.pop()
        
        return S == T