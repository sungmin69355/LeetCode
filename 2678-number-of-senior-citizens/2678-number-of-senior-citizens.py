class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        result = 0
        
        for index in details:
            if int(index[11:13]) > 60:
                result+=1
        return result