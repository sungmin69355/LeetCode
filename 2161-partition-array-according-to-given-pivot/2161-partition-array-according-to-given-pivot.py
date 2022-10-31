class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, r, pi = [], [], []
        
        for i in nums: 
            if i < pivot:
                r.append(i)
            elif i ==  pivot:
                pi.append(i)
            else:
                l.append(i)
                
        return r+pi+l
                