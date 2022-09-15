# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr=head
        n=-1
        while curr:
            n+=1
            curr=curr.next
            
        curr=head
        res=0
        while curr:
            res+=curr.val*(2**n)
            n-=1
            curr=curr.next
        
        return res