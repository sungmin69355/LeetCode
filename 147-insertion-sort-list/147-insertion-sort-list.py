# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p = head
        
        Node_list = []
        
        while p:
            Node_list.append(p.val)
            p = p.next
        
        Node_list.sort()
        p = head
        
        for i in range(len(Node_list)):
            p.val = Node_list[i]
            p = p.next
        
        return head
        
        
        