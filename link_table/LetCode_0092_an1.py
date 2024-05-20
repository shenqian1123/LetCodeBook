
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ## 利用stack存储left right之间的Node
        stack = list()
        dummy_head = ListNode(0, head)
        p = dummy_head
        p_l = None
        p_r = None
        n = 0
        while True:
            if not p:
                break
            if n == right:
                p_r = p.next
            if n == left - 1:
                p_l = p
                stack.append(p.next)
            if left <= n < right:
                stack.append(p.next)
            n = n + 1
            p = p.next
        dummy_head1 = ListNode(0)
        pB = dummy_head1
        while stack:
            p = stack.pop()
            p.next = None
            pB.next = p
            pB = pB.next
        p_l.next = dummy_head1.next
        pB.next = p_r
        return dummy_head.next
            
if __name__ == "__main__":
    sl = Solution()
    l1 = ListNode(3)
    l1.next = ListNode(5)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = sl.reverseBetween(l1, 1, 2)
    while True:
        if result:
            print(result.val)
            result = result.next
        else:
            break