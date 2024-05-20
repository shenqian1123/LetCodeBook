
from typing import Optional

## 反转链表，迭代方法

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## 使用迭代的方法
        p = head
        prev = None
        while True:
            if not p:
                break
            temp = p.next
            p.next = prev
            prev = p
            p = temp

        return prev