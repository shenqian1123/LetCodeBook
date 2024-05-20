from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## 先获取尾部的Node
        p_end = head
        while True:
            if not p_end or not p_end.next:
                break
            p_end = p_end.next

        ## p_end_temp标志循环结束
        p_end_temp = p_end
        prev = head
        p = prev.next if prev else None
        while True:
            ## 奇数长度
            if prev == p_end_temp:
                break
            ## 长度为2
            if p == p_end_temp and not p.next:
                break
            ## move
            prev.next = p.next
            p_end.next = p
            p.next = None
            ## 偶数长度
            if p == p_end_temp:
                break
            
            prev = prev.next
            p = prev.next if prev else None
            p_end = p_end.next


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