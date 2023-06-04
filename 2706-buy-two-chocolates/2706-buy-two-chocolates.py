from itertools import combinations

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        twoChocolates = list(combinations(prices, 2))
        
        result = []
        for i in range(len(twoChocolates)):
            if twoChocolates[i][0] + twoChocolates[i][1] <= money:
                result.append(twoChocolates[i][0] + twoChocolates[i][1])
                
        if len(result) > 0:
            return money - min(result)
        
        return money
