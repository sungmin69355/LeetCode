class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        result = set()
        
        while n not in result:
            result.add(n)
            arr =list(str(n))
            print(result)
            sum =0
            for i in range(len(arr)):
                sum += int(arr[i])**2
            
            arr = []
            n = sum
            if sum == 1:
                return True
            
        
        return False