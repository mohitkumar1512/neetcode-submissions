# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while True:
            if not fast or not fast.next:
                break
            slow = slow.next
            fast = fast.next.next
        

        prev = None
        curr = slow
        while curr:
            next_node = curr.next  
            curr.next = prev       
            prev = curr            
            curr = next_node 
        second = head

        while second:
            temp1 = second.next
            temp2 = prev.next
            second.next = prev
            prev.next = temp1
            prev = temp2
            second = temp1



