from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
## 双指针+队列
## 把list1往list2合并
## 给list2创建dummy_head
## 让pB初始指向dummy_head
## 让pA初始指向list1
## cond1 : 如果找到pA.val在pB.val和pB.next.val之间，将这个Node放入stack
## 如果stack为空，则表示找不到以pA为起始Node的一段链表，它们满足cond1，那么pB来到pB.next这个Node
## 如果stack不为空，则表示找到了以pA为起始Node的一段链表，它们满足cond1，那么只需要将stack的最后一个元素的next指向pB.next，并让stack的第一个元素称为pB的后继即可
## 直到pB走到空节点


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head2 = ListNode(-101, list2)
        pA = list1
        pB = dummy_head2
        if not list1:
            return list2
        if not list2:
            return list1
        while True:
            if not pB:
                break
            min_b = pB.val if pB else -101
            max_b = pB.next.val if pB.next else 101

            tempA = list()
            while True:
                if (pA) and (min_b <= pA.val <= max_b):
                    tempA.append(pA)
                    pA = pA.next
                else:
                    break
            if len(tempA) != 0:
                tempA[-1].next = pB.next
                pB.next = tempA[0]
                pB = tempA[-1].next
            else:
                pB = pB.next
        return dummy_head2.next

                    
