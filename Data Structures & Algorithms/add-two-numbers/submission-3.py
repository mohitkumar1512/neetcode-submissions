# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1C = l1
        # l2C = l2
        # sumTotal = 0
        # multiplier = 1
        # while l1C:
        #     sumTotal += (l1C.val * multiplier)
        #     l1C = l1C.next
        #     multiplier *= 10
        
        # multiplier = 1
        # while l2C:
        #     sumTotal += (l2C.val * multiplier)
        #     l2C = l2C.next
        #     multiplier *= 10
        
        # newLinkList = ListNode(0)
        # if sumTotal == 0:
        #     return newLinkList
        # copy = newLinkList
        # while sumTotal != 0:
        #     copy.next = ListNode(sumTotal % 10)
        #     copy = copy.next
        #     sumTotal = sumTotal // 10

        # return newLinkList.next
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next