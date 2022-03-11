# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node_list = []
        p = head
        while p:
            node_list.append(p.val)
            p = p.next
        node_list.sort()
        
        p=head
        for i in range(len(node_list)):
            p.val = node_list[i]
            p = p.next
            
        return head
        