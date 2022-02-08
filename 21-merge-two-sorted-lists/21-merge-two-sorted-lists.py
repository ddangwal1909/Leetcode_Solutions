# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        tmp=head
        while l1 and l2:
            if l1.val<=l2.val:
                tmp.next = l1
                l1= l1.next
            else:
                tmp.next = l2
                l2=l2.next
            tmp=tmp.next
        
        while l2:
            tmp.next = l2
            l2 = l2.next
            tmp=tmp.next
        
        while l1:
            tmp.next = l1
            l1 = l1.next
            tmp = tmp.next
            
        return head.next
            
                
        