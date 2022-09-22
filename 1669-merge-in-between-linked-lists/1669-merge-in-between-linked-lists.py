# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr=list1
        for i in range(a-1):
            curr=curr.next
        start=curr
        curr=curr.next
        for i in range(a,b+1):
            if curr is None:
                break
            else:
                curr=curr.next
        end=curr
        start.next=list2
        curr=list2
        while curr.next:
            curr=curr.next
        curr.next=end
        
        return list1