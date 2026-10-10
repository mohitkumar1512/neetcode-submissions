# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode(0)
        dummy_copy = dummy

        while list1 and list2: 
            if list1.val < list2.val: 
                dummy_copy.next = list1
                list1 = list1.next
            else:
                dummy_copy.next = list2
                list2 = list2.next
            dummy_copy = dummy_copy.next
        
        
        dummy_copy.next = list1 or list2
        return dummy.next

            