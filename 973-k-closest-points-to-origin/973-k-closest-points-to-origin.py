class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def closest(i):
            return i[0]*i[0] + i[1]*i[1]
        
        sorted_points = sorted(points, key=closest)
 
        return sorted_points[:k]
        
        