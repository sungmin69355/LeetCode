# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur, res = head, []
    
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        n, max_sum = len(res), 0
    
        k = []
        for i in range(n):
            k.append(res[i] + res[n-1-i])
        
        return max(k)