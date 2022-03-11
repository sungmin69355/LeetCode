class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []
        start, end = intervals[0]
        
        for st, en in intervals[1:]:
            
            if st <= end:    
                if en > end:
                    end = en
            else:
                res.append([start, end])
                start = st
                end = en
                
        res.append([start, end])
        return res