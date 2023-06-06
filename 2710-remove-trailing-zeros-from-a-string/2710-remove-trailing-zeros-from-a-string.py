
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        result = list(num)
        for _ in range(len(num)):
            a = result.pop()
            if a != "0":
                result.append(a)
                return ''.join(result)