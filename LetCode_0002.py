# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        l1_cur = l1
        l2_cur = l2
        result_cur = result
        while True:
            if l1_cur and l2_cur:
                add_res = l1_cur.val + l2_cur.val
            elif l1_cur or l2_cur:
                add_res = l1_cur.val if l1_cur else l2_cur.val
            else:
                break
            if result:
                if result_cur.next:
                    result_cur.next = ListNode(add_res + result_cur.next.val - 10, ListNode(1)) if add_res + result_cur.next.val > 9 else ListNode(add_res + result_cur.next.val)
                else:
                    result_cur.next = ListNode(add_res - 10, ListNode(1)) if add_res > 9 else ListNode(add_res)
                result_cur = result_cur.next
            else:
                result = ListNode(add_res - 10, ListNode(1)) if add_res > 9 else ListNode(add_res)
                result_cur = result
            if not result_cur:
                break
            
            l1_cur = l1_cur.next if l1_cur else None
            l2_cur = l2_cur.next if l2_cur else None

        return result

if __name__ == "__main__":
    sl = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = sl.addTwoNumbers(l1, l2)
    while True:
        print(result.val)
        result = result.next
        if not result.next:
            print(result.val)
            break
    print(result)

            
