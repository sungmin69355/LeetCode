class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        num = x ^ y
        while(num > 0):
            count += (num & 1)
            num = num >> 1
        return count