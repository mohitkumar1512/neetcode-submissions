# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        if not list1 and not list2: 
            return None

        dummy = ListNode(0)
        dummy_copy = dummy

        while list1 and list2: 
            if list1.val < list2.val: 
                dummy_copy.next = ListNode(list1.val)
                list1 = list1.next
            else:
                dummy_copy.next = ListNode(list2.val)
                list2 = list2.next
            dummy_copy = dummy_copy.next
        
        while list1: 
            dummy_copy.next = ListNode(list1.val)
            list1 = list1.next
            dummy_copy = dummy_copy.next
        while list2: 
            dummy_copy.next = ListNode(list2.val)
            list2 = list2.next
            dummy_copy = dummy_copy.next
        return dummy.next

            