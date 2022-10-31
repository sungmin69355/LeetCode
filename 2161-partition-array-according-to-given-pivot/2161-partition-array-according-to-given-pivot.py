class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, r, pi = [], [], []
        
        for i in nums: 
            if i < pivot:
                l.append(i)
            elif i ==  pivot:
                pi.append(i)
            else:
                r.append(i)
                
        return l+pi+r
                