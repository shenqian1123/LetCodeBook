from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummyHead = ListNode(0, head)
        # p = dummyHead
        # while True:
        #     if not p or not p.next:
        #         break
        #     if p.next.val == val:
        #         p.next = p.next.next
        #         # p.next.next = None
        #     else:
        #         p = p.next
        # return dummyHead.next
        if (not head):
            return head
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next
if __name__ == "__main__":
    sl = Solution()
    l1 = ListNode(7)
    l1.next = ListNode(7)
    l1.next.next = ListNode(7)
    l1.next.next.next = ListNode(6)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = sl.removeElements(l1, 7)
    while True:
        if result:
            print(result.val)
            result = result.next
        else:
            break