class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_a, cost_b = 0, 0
        for i in cost:
            cost_a, cost_b = min(cost_a, cost_b)+i, cost_a
        
        return min(cost_a, cost_b)