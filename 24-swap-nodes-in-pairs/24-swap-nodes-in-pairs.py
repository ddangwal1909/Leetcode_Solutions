# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev=ListNode(0)
        new_head=prev
        curr=head
        
        if curr is None or curr.next is None:
            return head
        
        nxt=head.next
        
        
        while nxt:
            tmp = nxt.next
            nxt.next=curr
            curr.next=tmp
            prev.next=nxt
            prev=curr
            curr=curr.next
            if curr is None:
                nxt=None
            else:
                nxt=curr.next
        
        return new_head.next
        
        
        
        
        
        
        
        
        