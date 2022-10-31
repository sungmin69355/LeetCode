class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = list(tiles)
        result = 0
        for i in range(len(cnt)):
            printCnt = set(list(permutations(cnt, i+1)))
            result += len(printCnt)
        return result
