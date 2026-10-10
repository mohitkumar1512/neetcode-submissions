# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1C = l1
        l2C = l2
        sumTotal = 0
        multiplier = 1
        while l1C:
            sumTotal += (l1C.val * multiplier)
            l1C = l1C.next
            multiplier *= 10
        
        multiplier = 1
        while l2C:
            sumTotal += (l2C.val * multiplier)
            l2C = l2C.next
            multiplier *= 10
        
        newLinkList = ListNode(0)
        if sumTotal == 0:
            return newLinkList
        copy = newLinkList
        while sumTotal != 0:
            copy.next = ListNode(sumTotal % 10)
            copy = copy.next
            sumTotal = sumTotal // 10

        return newLinkList.next
