# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr, curr_next = head, head

        while curr_next and curr_next.next:
            curr = curr.next
            curr_next = curr_next.next.next
            if curr == curr_next:
                return True
        return False