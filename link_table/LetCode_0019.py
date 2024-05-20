from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        pA = dummy_head
        pB = dummy_head
        pA_step = 0
        while True:
            if not pA.next:
                pB.next = pB.next.next
                break
            if pA_step >= n:
                pB = pB.next
            pA = pA.next
            pA_step = pA_step + 1
        return dummy_head.next
    
    def removeNthFromEnd_by_stack(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        cur = dummy_head
        stack = list()
        while cur:
            stack.insert(cur, 0)
            cur = cur.next
        for i in range(n):
            stack.pop(0)
        prev = stack[0]
        prev.next = prev.next.next
        return dummy_head.next
        