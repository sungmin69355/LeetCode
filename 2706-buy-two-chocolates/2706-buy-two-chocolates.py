from itertools import combinations

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a=min(prices)
        prices.remove(a)
        
        b=min(prices)
        new=money-a-b
        
        if(a+b>money):
            return money
        else:
            return new