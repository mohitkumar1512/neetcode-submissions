# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        head_copy = head
        while head_copy: 
            temp = head_copy.next
            head_copy.next = prev
            prev = head_copy            
            head_copy = temp            
        return prev
            