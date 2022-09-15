# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dictionary={}
        curr=head
        str1=''
        while curr:
            str1+=chr(ord('0')+curr.val)
            curr=curr.next
        
        if str1==str1[::-1]:
            return True
        else:
            return False