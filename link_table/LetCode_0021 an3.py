from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## 链表解法
## 解决一个最小模型问题，其他不同规模的子问题可以使用递归进行求解
## 递归的每种case需要向上返回信息

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2
        if not list1 and not list2:
            return None
        return self.merge(list1, list2)

    def merge(self, list1, list2):
        if not list1 or not list2:
            return list1 if list1 else list2
        if list1.val <= list2.val:
            list1.next = self.merge(list1.next, list2)
            return list1
        else:
            list2.next = self.merge(list1, list2.next)
            return list2
                    
