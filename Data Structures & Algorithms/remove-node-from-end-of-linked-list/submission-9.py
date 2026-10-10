# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length = 0
        # dummy = head
        # while dummy:
        #     length += 1
        #     dummy = dummy.next

        # if length == 1 or length == 0:
        #     return None 

        # if length == n:
        #     return head.next
       
        # toRemove = length - n + 1

        # prev = None
        # curr = head
        # while toRemove > 1:
        #     prev = curr
        #     curr = curr.next
        #     toRemove -= 1
        
        # prev.next = curr.next if curr.next else None
        
        # return head
        
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        