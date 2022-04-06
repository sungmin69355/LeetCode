class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        pre1=1;
        pre2=0;
        for i in range(1,n+1):
            cur = pre1+pre2
            pre2 = pre1
            pre1 = cur
        return pre2