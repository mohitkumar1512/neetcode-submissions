# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited = {}
        # index = 0
        # while head != None:
        #     if visited and head in visited:
        #         return True
        #     else:
        #         visited[head] = index
        #         index += 1
        #         head = head.next if head else None
        # return False

        # using a two pointer approach
        curr, curr_next = head, head

        while curr_next and curr_next.next:
            curr = curr.next
            curr_next = curr_next.next.next
            if curr == curr_next:
                return True
        return False