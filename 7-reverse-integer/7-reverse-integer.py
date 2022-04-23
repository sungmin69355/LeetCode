class Solution:
    def reverse(self, x: int) -> int:
        
        if x > 0:
            v =  int(str(x)[::-1])
        else:
            v = -int(str(x*-1)[::-1])
            
        if v not in range(-2**31,2**31): #Overflow 
            v = 0
            
        return v