from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
## 双指针
## 先创建dummy_head，并让prev指向dummy_head
## 创建pA,pB分别指向list1和list2的head
## pA.val和pB.val进行比较，谁小谁就称为prev.next
## prev = prev.next
## 小值的Node指针后移
## pA和pB有一个为None退出循环
## 将pA和pB中不为None的Node作为perv.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        pA = list1
        pB = list2
        prev = dummy_head
        while True:
            if not pA or not pB:
                break
            if pA.val <= pB.val:
                prev.next = pA
                prev = prev.next
                pA = pA.next
            else:
                prev.next = pB
                prev = prev.next
                pB = pB.next
        prev.next = pA if pA else pB
    
        return dummy_head.next
                    
