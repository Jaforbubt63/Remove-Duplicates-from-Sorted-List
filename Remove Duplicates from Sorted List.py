# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        nodes = set()
        nodes.add(head.val)
        
        prev = head
        node = head.next
        
        while node:
            if node.val in nodes:
                prev.next = node.next
                node = prev.next
                continue
                
            prev = node
            node = node.next
            
        return head
                
            
        