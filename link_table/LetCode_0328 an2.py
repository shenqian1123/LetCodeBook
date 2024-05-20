from typing import Optional

## 将链表的奇偶节点分成奇数链表和偶数链表
## 完成上述操作后在将偶数链表接到奇数链表之后

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head



if __name__ == "__main__":
    sl = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = sl.oddEvenList(l1)
    while True:
        print(result.val)
        result = result.next
        if not result.next:
            print(result.val)
            break
    print(result)