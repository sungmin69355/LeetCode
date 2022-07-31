# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def add(data):
            node = result
            while node.next:
                node = node.next
            node.next = ListNode(data)
            
        temp = []
        while head is not None:
            temp.append(head.val)
            head = head.next
        
        temp = temp[int(len(temp)/2):]
        
        result = ListNode(temp[0])
        for i in range(1, len(temp)):
            add(temp[i])
            
        return result