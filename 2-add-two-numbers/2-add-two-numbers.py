# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = self.toList(self.reverseList(l1))
        l2_list = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(s) for s in l1_list)) + int(''.join(str(s) for s in l2_list));
        
        return self.toReverseLinkedList(str(resultStr));
        
    def reverseList(self, head: ListNode)-> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def toList(self, node: ListNode) ->List:
        list: List =[]
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    def toReverseLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for i in result:
            node = ListNode(i)
            node.next = prev
            prev = node
            
        return node
        