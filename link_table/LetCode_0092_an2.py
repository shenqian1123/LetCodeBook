
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ## 将left和right之间的Node使用反转链表的方法进行反转
        ## 然后将存储的left左侧Node和right右侧Node进行连接
        p = head
        prev = None
        n = 0
        p_l = None
        p_r = None
        while True:
            if not p:
                break
            n = n + 1
            if n == left - 1:
                p_l = p
            if left < n <= right:
                temp = p.next
                p.next = prev
                prev = p
                p = temp
            else:
                prev = p
                p = p.next                
            if n == right:
                p_r = p
                break
        if p_l:
            p_l.next.next = p
            p_l.next = prev
            return head
        elif prev == head:
            # head.next = None
            return prev
        else:
            head.next = p
            return prev


            


            
if __name__ == "__main__":
    sl = Solution()
    l1 = ListNode(3)
    l1.next = ListNode(5)
    # l1.next.next = ListNode(2, ListNode(5, ListNode(4, ListNode(3, ListNode(6)))))
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = sl.reverseBetween(l1, 1, 1)
    while True:
        if result:
            print(result.val)
            result = result.next
        else:
            break