class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        if self.head:
            headCopy = self.head
            while headCopy:
                if not index:
                    return headCopy.val
                headCopy = headCopy.next
                index -= 1
        return -1
    
    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
    
    def insertTail(self, val: int) -> None:
        if self.head:
            headCopy = self.head
            prev = self.head
            while headCopy:
                prev = headCopy
                headCopy = headCopy.next
            
            prev.next = ListNode(val)
            return
        self.head = ListNode(val)

    def remove(self, index: int) -> bool:
        if self.head:
            headCopy = self.head
            prev = None
            while headCopy:
                if index == 0:
                    if prev:
                        prev.next = headCopy.next
                    else:
                        self.head = self.head.next
                    return True
                prev = headCopy
                headCopy = headCopy.next
                index -= 1
        return False

    def getValues(self) -> List[int]:
        res = []
        headCopy = self.head
        while headCopy:
            res.append(headCopy.val)
            headCopy = headCopy.next
        return res
